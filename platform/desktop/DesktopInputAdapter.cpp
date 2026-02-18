#include "DesktopInputAdapter.h"

namespace pvz::platform::desktop {

bool DesktopInputAdapter::IsKeyDown(int /*keycode*/) const
{
    return false;
}

bool DesktopInputAdapter::IsMouseButtonDown(MouseButton /*button*/) const
{
    return false;
}

int DesktopInputAdapter::GetMouseX() const
{
    return 0;
}

int DesktopInputAdapter::GetMouseY() const
{
    return 0;
}

} // namespace pvz::platform::desktop
