#include "LawnAppRunner.h"
#include "LawnGlobals.h"

#include "LawnApp.h"
#include "Resources.h"
#include "Sexy.TodLib/TodStringFile.h"

using namespace Sexy;

namespace pvz::app {

int RunLawnApp(platform::IFileSystem& fileSystem, platform::IClock& clock)
{
    const auto startupBeginMs = clock.NowMilliseconds();

    TodStringListSetColors(gLawnStringFormats, gLawnStringFormatCount);
    gGetCurrentLevelName = LawnGetCurrentLevelName;
    gAppCloseRequest = LawnGetCloseRequest;
    gAppHasUsedCheatKeys = LawnHasUsedCheatKeys;
    gExtractResourcesByName = Sexy::ExtractResourcesByName;

    gLawnApp = new LawnApp();
    gLawnApp->mChangeDirTo = (!fileSystem.Exists("properties\\resources.xml") && fileSystem.Exists("..\\properties\\resources.xml")) ? ".." : ".";
    gLawnApp->Init();

    // Keep this marker for later baseline logging integration in Phase 0 runtime capture.
    const auto startupReadyMs = clock.NowMilliseconds() - startupBeginMs;
    (void)startupReadyMs;

    gLawnApp->Start();
    gLawnApp->Shutdown();

    if (gLawnApp)
        delete gLawnApp;

    return 0;
}

} // namespace pvz::app
