# docker-autobuild

在官方的 docker images 中增加一些必要的软件、拓展、工具，来便于自己的开发

> 所有的镜像都基于 Dockerfile 自动构建，请放心查阅使用

## Tags

### rovast/php

|            | rovast/php:7.2-fpm                    | rovast/php:7.2-cli                    |
| ---------- | ------------------------------------- | ------------------------------------- |
| php-extensions | mongodb、redis、zip                   | mongodb、redis、zip                   |
| software   | curl、composer、cron、zip、unzip、git | curl、composer、cron、zip、unzip、git |

### rovast/gcc

|            | rovast/gcc:8                    |
| ---------- | ------------------------------- |
| software   | gdb |

