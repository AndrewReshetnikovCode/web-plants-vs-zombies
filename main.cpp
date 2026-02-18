#include "LawnApp.h"
#include "Resources.h"
#include "Sexy.TodLib/TodStringFile.h"
#include "app/LawnAppRunner.h"
#include "app/LawnGlobals.h"
#include "platform/desktop/DesktopClockAdapter.h"
#include "platform/desktop/DesktopFileSystemAdapter.h"
#include "platform/desktop/DesktopInputAdapter.h"
#include "platform/desktop/DesktopWindowAdapter.h"

using namespace Sexy;

bool (*gAppCloseRequest)();             //[0x69E6A0]
bool (*gAppHasUsedCheatKeys)();         //[0x69E6A4]
SexyString (*gGetCurrentLevelName)();

namespace {
int RunDesktopEntry()
{
    pvz::platform::desktop::DesktopFileSystemAdapter fileSystem;
    pvz::platform::desktop::DesktopClockAdapter clock;
    pvz::platform::desktop::DesktopWindowAdapter window(800, 600);
    pvz::platform::desktop::DesktopInputAdapter input;
    return pvz::app::RunLawnApp(fileSystem, clock, window, input);
}
} // namespace

//0x44E8F0
#if defined(_WIN32)
int WINAPI WinMain(_In_ HINSTANCE /* hInstance */, _In_opt_ HINSTANCE /* hPrevInstance */, _In_ LPSTR /* lpCmdLine */, _In_ int /* nCmdShow */)
{
    return RunDesktopEntry();
}
#else
int main(int /*argc*/, char** /*argv*/)
{
    return RunDesktopEntry();
}
#endif
