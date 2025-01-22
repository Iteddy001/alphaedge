import subprocess
import winreg
import os

class AlphaEdge:
    def __init__(self):
        print("Initializing AlphaEdge: Strengthening Windows Privacy Settings")

    def disable_telemetry(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\DataCollection", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "AllowTelemetry", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print("Telemetry disabled.")
        except Exception as e:
            print(f"Failed to disable telemetry: {e}")

    def disable_cortana(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "AllowCortana", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print("Cortana disabled.")
        except Exception as e:
            print(f"Failed to disable Cortana: {e}")

    def disable_location_tracking(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\lfsvc\Service\Configuration", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "Status", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print("Location tracking disabled.")
        except Exception as e:
            print(f"Failed to disable location tracking: {e}")

    def disable_ad_id(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "Enabled", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print("Advertising ID disabled.")
        except Exception as e:
            print(f"Failed to disable Advertising ID: {e}")

    def run(self):
        self.disable_telemetry()
        self.disable_cortana()
        self.disable_location_tracking()
        self.disable_ad_id()
        print("All privacy settings have been configured.")

if __name__ == "__main__":
    alpha_edge = AlphaEdge()
    alpha_edge.run()