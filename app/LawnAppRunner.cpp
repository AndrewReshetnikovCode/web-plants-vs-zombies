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

    window.SetTitle("Plants vs. Zombies");
    window.SetCursorVisible(true);
    (void)input.IsKeyDown(0);

    gLawnApp = new LawnApp();
    gLawnApp->mChangeDirTo = (!fileSystem.Exists("properties\\resources.xml") && fileSystem.Exists("..\\properties\\resources.xml")) ? ".." : ".";
    gLawnApp->Init();
    const std::uint64_t startupReadyMs = clock.NowMilliseconds();
    (void)startupReadyMs;
    gLawnApp->Start();
    gLawnApp->Shutdown();

    if (gLawnApp)
        delete gLawnApp;

    return 0;
}

} // namespace pvz::app
