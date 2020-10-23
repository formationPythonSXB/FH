import json
from infra_api import Infra

infra = Infra("http://127.0.0.1:5000")
print(infra.list())
print(infra.get("google"))
print(infra.create(name="test", owner="XxDarKLorDxX", os="windoze", ram=64))
# infra.start("test")
# assert infra.get("test")["state"] == "up"
# infra.stop("test")
# assert infra.get("test")["state"] == "down"
# infra.delete("test")