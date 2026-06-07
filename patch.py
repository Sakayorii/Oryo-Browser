import os
import io
import stat

def make_writable(path):
    if os.path.exists(path):
        os.chmod(path, stat.S_IWRITE)

def patch_file(path, old_text, new_text):
    full_path = os.path.join(r'D:\chromium_project\chromium\src', path)
    if not os.path.exists(full_path):
        print(f"NOT FOUND: {full_path}")
        return
    
    make_writable(full_path)
    
    with io.open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with io.open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"PATCHED: {path}")
    else:
        print(f"TEXT NOT FOUND IN: {path}")

# 3. Cursor
patch_file('ui/base/cursor/cursor_factory.cc',
'''scoped_refptr<PlatformCursor> CursorFactory::GetDefaultCursor(
    mojom::CursorType type) {''',
'''scoped_refptr<PlatformCursor> CursorFactory::GetDefaultCursor(
    mojom::CursorType type) {
  if (type == mojom::CursorType::kPointer) {
    int resource_id = IDR_CUSTOM_ORYO_CURSOR_POINTER;
    gfx::ImageSkia* image = ui::ResourceBundle::GetSharedInstance().GetImageSkiaNamed(resource_id);
    if (image) return CreateImageCursor(*image, gfx::Point(0, 0));
  }''')

# 4. Renderer Client
patch_file('chrome/renderer/chrome_content_renderer_client.cc',
'''void ChromeContentRendererClient::RenderFrameCreated(
    content::RenderFrame* render_frame) {''',
'''void ChromeContentRendererClient::RenderFrameCreated(
    content::RenderFrame* render_frame) {
  blink::WebLocalFrame* frame = render_frame->GetWebFrame();
  if (frame) {
    frame->ExecuteScript(blink::WebString::FromUTF8("window.__oryo_api = { init: true };"));
  }''')

# 5. Metrics
patch_file('components/metrics/metrics_service.cc',
'''void MetricsService::Start() {''',
'''void MetricsService::Start() {
  return;''')

# 6. Performance Manager
patch_file('components/performance_manager/performance_manager_impl.cc',
'''#include "base/process/process.h"''',
'''#include "base/process/process.h"

void PerformanceManagerImpl::ToggleGamingMode(bool enabled) {
  if (enabled) {
    base::Process::Current().SetPriority(base::Process::Priority::kBestEffort);
  } else {
    base::Process::Current().SetPriority(base::Process::Priority::kUserBlocking);
  }
}''')

# 7. Discord RPC
patch_file('chrome/browser/profiles/profile.cc',
'''#include <windows.h>''',
'''#include <windows.h>

void UpdateDiscordRichPresence(const std::string& active_media_title) {
  HANDLE hPipe = CreateFile(TEXT("\\\\\\\\.\\\\pipe\\\\discord-ipc-0"),
                            GENERIC_READ | GENERIC_WRITE,
                            0, NULL, OPEN_EXISTING, 0, NULL);
  if (hPipe != INVALID_HANDLE_VALUE) {
    std::string payload = "{\\"cmd\\":\\"SET_ACTIVITY\\",\\"args\\":{\\"pid\\":" + std::to_string(GetCurrentProcessId()) + ",\\"activity\\":{\\"details\\":\\"Watching: " + active_media_title + "\\"}}}";
    DWORD bytesWritten;
    WriteFile(hPipe, payload.c_str(), payload.length(), &bytesWritten, NULL);
    CloseHandle(hPipe);
  }
}''')
