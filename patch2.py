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

# safe_browsing_network_context.cc
patch_file('components/safe_browsing/content/browser/safe_browsing_network_context.cc',
'''  void CreateLoaderAndStart(
      mojo::PendingReceiver<network::mojom::URLLoader> loader,
      int32_t request_id,
      uint32_t options,
      const network::ResourceRequest& request,
      mojo::PendingRemote<network::mojom::URLLoaderClient> client,
      const net::MutableNetworkTrafficAnnotationTag& traffic_annotation)
      override {
    DCHECK(content::BrowserThread::CurrentlyOn(content::BrowserThread::UI));
    GetURLLoaderFactory()->CreateLoaderAndStart(
        std::move(loader), request_id, options, request, std::move(client),
        traffic_annotation);
  }''',
'''  void CreateLoaderAndStart(
      mojo::PendingReceiver<network::mojom::URLLoader> loader,
      int32_t request_id,
      uint32_t options,
      const network::ResourceRequest& request,
      mojo::PendingRemote<network::mojom::URLLoaderClient> client,
      const net::MutableNetworkTrafficAnnotationTag& traffic_annotation)
      override {
    return;
  }''')

# component_updater_service.cc
patch_file('components/component_updater/component_updater_service.cc',
'''void CrxUpdateService::Start() {
  DCHECK_CALLED_ON_VALID_SEQUENCE(sequence_checker_);''',
'''void CrxUpdateService::Start() {
  return;
  DCHECK_CALLED_ON_VALID_SEQUENCE(sequence_checker_);''')
