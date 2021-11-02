Project: /blueberry/_project.yaml
Book: /blueberry/_book.yaml

# Bluetooth Test Interfaces Summary

The Bluetooth test interfaces are Remote Procedure Call (RPC) interfaces
exposed to testing tools to trigger behaviors within a Bluetooth stack under
test. They are built using the following [requirements](
/blueberry/reference/doc/overview) and [style guide](
/blueberry/reference/doc/style-guide).

A test interface is defined for each Bluetooth profile. They currently include:

* [Host API](/blueberry/reference/host).
* [A2DP API](/blueberry/reference/a2dp).
