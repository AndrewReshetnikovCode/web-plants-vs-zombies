#pragma once

#include "platform/interfaces/IClock.h"
#include "platform/interfaces/IFileSystem.h"

namespace pvz::app {

int RunLawnApp(platform::IFileSystem& fileSystem, platform::IClock& clock);

} // namespace pvz::app
