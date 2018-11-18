#ifndef __VERSION_H__
#define __VERSION_H__

#define PLUGIN_NAME    "Mupen64Plus Bot Input Plugin"
#define PLUGIN_VERSION           0x000001
#define INPUT_PLUGIN_API_VERSION 0x020000

#define VERSION_PRINTF_SPLIT(x) (((x) >> 16) & 0xffff), (((x) >> 8) & 0xff), ((x) & 0xff)

#endif /* #define __VERSION_H__ */
