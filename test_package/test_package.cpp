#include "openvr.h"
#include <iostream>

int main()
{
  std::cout << "HMD present: " << vr::VR_IsHmdPresent() << "\n";
  std::cout << "Runtime installed: " << vr::VR_IsRuntimeInstalled() << "\n";
  return 0;
}
