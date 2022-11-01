# 注意事项 :warning:

:one: gdb 在 docker 里使用，需要注意一些启动参数，以下给出 docker-compose 的范例。

注意 **security_opt** 和 **cap_add** 配置

```yaml
version: '2'

services:
  gcc:
    image: rovast/gcc:8
    container_name: my-gcc
    security_opt:
      - seccomp:unconfined
    cap_add:
      - SYS_PTRACE
    volumes:
      - /home/rovast/Code:/home/Code
      - ./README.md:/home/README.md
    command: tail -f /home/README.md
```

正确挂载自己的代码目录到 /home/Code 即可

```bash
docker-compose up -d
docker exec -it my-gcc bash
```
