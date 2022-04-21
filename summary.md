Project: /pandora/_project.yaml
Book: /pandora/_book.yaml

# Bluetooth Test Interfaces Summary

The Bluetooth test interfaces are Remote Procedure Call (RPC) interfaces
exposed to testing tools to trigger behaviors within a Bluetooth stack under
test. They are built using the following [requirements](
/pandora/reference/doc/overview) and [style guide](
/pandora/reference/doc/style-guide).

A test interface is defined for each Bluetooth profile. They currently include:

* [Host API](/pandora/reference/host).
* [A2DP API](/pandora/reference/a2dp).
