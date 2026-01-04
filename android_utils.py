from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass, cast
    from android.runnable import run_on_ui_thread

    # Android classes
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Dialog = autoclass('android.app.Dialog')
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
    Color = autoclass('android.graphics.Color')

    class AndroidWebView:
        def __init__(self):
            self.dialog = None
            self.webview = None

        @run_on_ui_thread
        def open_url(self, url):
            activity = PythonActivity.mActivity
            
            # Create WebView
            self.webview = WebView(activity)
            self.webview.getSettings().setJavaScriptEnabled(True)
            self.webview.getSettings().setUseWideViewPort(True)
            self.webview.getSettings().setLoadWithOverviewMode(True)
            self.webview.getSettings().setBuiltInZoomControls(True)
            self.webview.setWebViewClient(WebViewClient())
            
            # Load URL
            self.webview.loadUrl(url)
            
            # Create Dialog to hold WebView
            self.dialog = Dialog(activity, 16973834) # Theme_Black_NoTitleBar_Fullscreen
            self.dialog.setContentView(self.webview)
            self.dialog.setCancelable(True)
            self.dialog.show()

else:
    # Mock class for non-Android platforms
    class AndroidWebView:
        def open_url(self, url):
            print(f"Mock AndroidWebView: Opening {url}")
