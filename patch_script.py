import os
import io

def inject_code(path, anchor, new_code):
    full_path = os.path.join(r'D:\chromium_project\chromium\src', path)
    if not os.path.exists(full_path):
        print(f'File not found: {full_path}')
        return
    with io.open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if anchor in content and new_code not in content:
        content = content.replace(anchor, anchor + '\n' + new_code)
        with io.open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Patched {path}')
    else:
        print(f'Could not patch {path}')

inject_code('ui/base/cursor/cursor_factory.cc',
'scoped_refptr<PlatformCursor> CursorFactory::GetDefaultCursor(\n    mojom::CursorType type) {',
'  if (type == mojom::CursorType::kPointer) {\n    int resource_id = IDR_CUSTOM_ORYO_CURSOR_POINTER;\n    gfx::ImageSkia* image = ui::ResourceBundle::GetSharedInstance().GetImageSkiaNamed(resource_id);\n    if (image) return CreateImageCursor(*image, gfx::Point(0, 0));\n  }')

inject_code('chrome/renderer/chrome_content_renderer_client.cc',
'void ChromeContentRendererClient::RenderFrameCreated(\n    content::RenderFrame* render_frame) {',
'  blink::WebLocalFrame* frame = render_frame->GetWebFrame();\n  if (frame) {\n    frame->ExecuteScript(blink::WebString::FromUTF8("window.__oryo_api = { init: true };"));\n  }')

inject_code('components/metrics/metrics_service.cc',
'void MetricsService::Start() {',
'  return;')

inject_code('chrome/browser/performance_manager/performance_manager_impl.cc',
'#include "base/process/process.h"',
'\nvoid PerformanceManagerImpl::ToggleGamingMode(bool enabled) {\n  if (enabled) {\n    base::Process::Current().SetPriority(base::Process::Priority::kBestEffort);\n  } else {\n    base::Process::Current().SetPriority(base::Process::Priority::kUserBlocking);\n  }\n}')

inject_code('chrome/browser/profiles/profile.cc',
'#include <windows.h>',
'\nvoid UpdateDiscordRichPresence(const std::string& active_media_title) {\n  HANDLE hPipe = CreateFile(TEXT("\\\\\\\\.\\\\pipe\\\\discord-ipc-0"),\n                            GENERIC_READ | GENERIC_WRITE,\n                            0, NULL, OPEN_EXISTING, 0, NULL);\n  if (hPipe != INVALID_HANDLE_VALUE) {\n    std::string payload = "{\\"cmd\\":\\"SET_ACTIVITY\\",\\"args\\":{\\"pid\\":" + std::to_string(GetCurrentProcessId()) + ",\\"activity\\":{\\"details\\":\\"Watching: " + active_media_title + "\\"}}}";\n    DWORD bytesWritten;\n    WriteFile(hPipe, payload.c_str(), payload.length(), &bytesWritten, NULL);\n    CloseHandle(hPipe);\n  }\n}')
