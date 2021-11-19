from enum import IntEnum


class StoveState(IntEnum):
    STATUS_OFF = 0
    STATUS_STARTING_1 = 1
    STATUS_STARTING_2 = 2
    STATUS_STARTING_3 = 3
    STATUS_STARTING_4 = 4
    STATUS_STARTING_5 = 5
    STATUS_STARTING_6 = 6
    STATUS_STARTING_7 = 7
    STATUS_POWER = 8
    STATUS_STOPPING_1 = 9
    STATUS_STOPPING_2 = 10
    STATUS_ECO_STOP_1 = 11
    STATUS_ECO_STOP_2 = 12
    STATUS_ECO_STOP_3 = 13
    STATUS_LOW_PELLET = 14
    STATUS_END_PELLET = 15
    STATUS_BLACK_OUT = 16
    STATUS_ANTI_FREEZE = 17
    STATUS_INGNITION_FAILED = 60
    STATUS_NO_PELLET = 61
    STATUS_COVER_OPEN = 69


class StoveChronoMode(IntEnum):
    CHRONO_OFF = 0
    CHRONO_SLEEP = 1
    CHRONO_ON_1 = 2
    CHRONO_ON_2 = 3
    CHRONO_ON_3 = 4
    CHRONO_ON_4 = 5


class StoveManufacturer(IntEnum):
    STOVE_MANUFACTURER_65 = 65
    STOVE_MANUFACTURER_76 = 76
    STOVE_MANUFACTURER_100 = 100


class StoveRegisters(IntEnum):
    ## Infos ##
    INDEX_FW = 1
    INDEX_WIFI = 2

    ## Data 0 ##
    INDEX_PAGE = 0
    INDEX_MANUFACTURER = 1
    INDEX_BITMAP_VISIBLE = 2
    INDEX_VALID = 3
    INDEX_STOVE_TYPE = 4
    INDEX_STOVE_STATE = 5
    INDEX_STOVE_ON = 6
    INDEX_ECO_MODE = 7
    INDEX_TIMER_ON = 8
    INDEX_AMBIENT_T1 = 9
    INDEX_AMBIENT_T1_SET = 10
    INDEX_AMBIENT_T1_SET_MIN = 11
    INDEX_AMBIENT_T1_SET_MAX = 12
    INDEX_AMBIENT_T2 = 13
    INDEX_AMBIENT_T2_SET = 14
    INDEX_AMBIENT_T2_SET_MIN = 15
    INDEX_AMBIENT_T2_SET_MAX = 16
    INDEX_WATER = 17
    INDEX_WATER_SET = 18
    INDEX_WATER_SET_MIN = 19
    INDEX_WATER_SET_MAX = 20
    INDEX_SMOKE_T = 21
    INDEX_POWER_LEVEL = 22
    INDEX_POWER_SET = 23
    INDEX_POWER_MIN = 24
    INDEX_POWER_MAX = 25
    INDEX_FAN_SMOKE = 26
    INDEX_FAN_1 = 27
    INDEX_FAN_1_SET = 28
    INDEX_FAN_1_SET_MAX = 29
    INDEX_FAN_2 = 30
    INDEX_FAN_2_SET = 31
    INDEX_FAN_2_SET_MAX = 32
    INDEX_FAN_3 = 33
    INDEX_FAN_3_SET = 34
    INDEX_FAN_3_SET_MAX = 35

    ## Data 1 Chrono ##
    INDEX_STATE = 1
    INDEX_TEMPERATURE_1 = 2
    INDEX_TEMPERATURE_1_MIN = 3
    INDEX_TEMPERATURE_1_MAX = 4
    INDEX_TEMPERATURE_2 = 5
    INDEX_TEMPERATURE_2_MIN = 6
    INDEX_TEMPERATURE_2_MAX = 7
    INDEX_TEMPERATURE_3 = 8
    INDEX_TEMPERATURE_3_MIN = 9
    INDEX_TEMPERATURE_3_MAX = 10

    ## Data 2 ##
    INDEX_FLOW_SWITCH = 1
    INDEX_GENERIC_PUMP = 2
    INDEX_AIREX_1 = 3
    INDEX_AIREX_2 = 4
    INDEX_AIREX_3 = 5
    INDEX_PUFFER = 6
    INDEX_PUFFER_SET = 7
    INDEX_PUFFER_SET_MIN = 8
    INDEX_PUFFER_SET_MAX = 9
    INDEX_BOILER = 10
    INDEX_BOILER_SET = 11
    INDEX_BOILER_SET_MIN = 12
    INDEX_BOILER_SET_MAX = 13
    INDEX_DHW = 14
    INDEX_DHW_SET = 15
    INDEX_DHW_SET_MIN = 16
    INDEX_DHW_SET_MAX = 17
    INDEX_ROOM_TEMP_3 = 18
    INDEX_ROOM_TEMP_3_SET = 19
    INDEX_ROOM_TEMP_3_SET_MIN = 20
    INDEX_ROOM_TEMP_3_SET_MAX = 21


class StoveCommands(IntEnum):
    PARAM_ON_OFF = 0
    PARAM_ECO_MODE = 1
    PARAM_NIVEAU_PUISSANCE = 2
    PARAM_AMBIANCE_TEMPERATURE_1 = 3
    INCONNU_4 = 4
    PARAM_NIVEAU_FAN_1 = 5
    PARAM_NIVEAU_FAN_2 = 6
    PARAM_NIVEAU_FAN_3 = 7
    PARAM_CHRONO_ON_OFF = 8
    PARAM_CHRONO_TEMPERATURE_1 = 9
    PARAM_CHRONO_TEMPERATURE_2 = 10
    PARAM_CHRONO_TEMPERATURE_3 = 11
