from pynvml import *


class NVIDIA(object):

    class MEM(object):
        def get_mem(self, unit, mtype):
            nvmlInit()
            handle = nvmlDeviceGetHandleByIndex(0)
            meminfo = nvmlDeviceGetMemoryInfo(handle)
            nvmlShutdown()

            def return_type(mtype):
                return {
                    'total': meminfo.total,
                    'free': meminfo.free,
                    'used': meminfo.used,
                }.get(mtype, 'error')

            return {
                'MB': round(return_type(mtype) / 1024 / 1024, 2),
                'GB': round(return_type(mtype) / 1024 / 1024 / 1024, 2),
            }.get(unit, 'error')

    def gpu_per(self):
        nvmlInit()
        per = nvmlDeviceGetUtilizationRates(nvmlDeviceGetHandleByIndex(0)).gpu
        return per

    def init_card(self):
        nvmlInit()

    def close_card(self):
        nvmlShutdown()

    def get_driver_version(self):
        self.init_card()
        ver = str(nvmlSystemGetDriverVersion().decode())
        self.close_card()
        return ver

    def get_card_info(self):
        self.init_card()
        card_info = []
        deviceCount = nvmlDeviceGetCount()
        for i in range(deviceCount):
            handle = nvmlDeviceGetHandleByIndex(i)
            card_info.append((i, nvmlDeviceGetName(handle).decode()))
        self.close_card()
        return card_info


if __name__ == '__main__':
    print(NVIDIA().gpu_per())
