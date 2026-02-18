#pragma once

#include "../interfaces/IInput.h"

namespace pvz::platform::desktop {

class DesktopInputAdapter : public IInput {
public:
    bool IsKeyDown(int keycode) const override;
    bool IsMouseButtonDown(MouseButton button) const override;
    int GetMouseX() const override;
    int GetMouseY() const override;
};

} // namespace pvz::platform::desktop
