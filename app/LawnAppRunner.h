#pragma once

#include "platform/interfaces/IClock.h"
#include "platform/interfaces/IFileSystem.h"
#include "platform/interfaces/IInput.h"
#include "platform/interfaces/IWindow.h"

namespace pvz::app {

int RunLawnApp(platform::IFileSystem& fileSystem, platform::IClock& clock, platform::IWindow& window, platform::IInput& input);

} // namespace pvz::app
