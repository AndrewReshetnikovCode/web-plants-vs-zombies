#include "LawnAppRunner.h"
#include "LawnGlobals.h"

#include "LawnApp.h"
#include "Resources.h"
#include "Sexy.TodLib/TodStringFile.h"

using namespace Sexy;

namespace pvz::app {

int RunLawnApp(platform::IFileSystem& fileSystem, platform::IClock& clock, platform::IWindow& window, platform::IInput& input)
{
    TodStringListSetColors(gLawnStringFormats, gLawnStringFormatCount);
    gGetCurrentLevelName = LawnGetCurrentLevelName;
    gAppCloseRequest = LawnGetCloseRequest;
    gAppHasUsedCheatKeys = LawnHasUsedCheatKeys;
    gExtractResourcesByName = Sexy::ExtractResourcesByName;

    // Startup seam hooks: keep these platform-facing calls in the runner path.
    window.SetTitle("Plants vs. Zombies");
    window.SetCursorVisible(true);
    const bool startupLeftDown = input.IsMouseButtonDown(platform::MouseButton::Left);
    const int startupMouseX = input.GetMouseX();
    const int startupMouseY = input.GetMouseY();
    TodTraceAndLog("Startup input marker: left=%d x=%d y=%d", startupLeftDown ? 1 : 0, startupMouseX, startupMouseY);

    const auto startupWindowSize = window.GetSize();

    gLawnApp = new LawnApp();
    gLawnApp->mWidth = startupWindowSize.width;
    gLawnApp->mHeight = startupWindowSize.height;
    gLawnApp->mChangeDirTo = (!fileSystem.Exists("properties\\resources.xml") && fileSystem.Exists("..\\properties\\resources.xml")) ? ".." : ".";
    gLawnApp->Init();
    window.SetFullscreen(!gLawnApp->mIsWindowed);
    const unsigned long long startupReadyMs = static_cast<unsigned long long>(clock.NowMilliseconds());
    TodTraceAndLog("Startup ready marker: %llu ms", startupReadyMs);
    gLawnApp->Start();
    gLawnApp->Shutdown();

    if (gLawnApp)
        delete gLawnApp;

    return 0;
}

} // namespace pvz::app
