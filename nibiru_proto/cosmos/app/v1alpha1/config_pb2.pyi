"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Config(google.protobuf.message.Message):
    """Config represents the configuration for a Cosmos SDK ABCI app.
    It is intended that all state machine logic including the version of
    baseapp and tx handlers (and possibly even Tendermint) that an app needs
    can be described in a config object. For compatibility, the framework should
    allow a mixture of declarative and imperative app wiring, however, apps
    that strive for the maximum ease of maintainability should be able to describe
    their state machine with a config object alone.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODULES_FIELD_NUMBER: builtins.int
    GOLANG_BINDINGS_FIELD_NUMBER: builtins.int
    @property
    def modules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ModuleConfig]:
        """modules are the module configurations for the app."""
    @property
    def golang_bindings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GolangBinding]:
        """golang_bindings specifies explicit interface to implementation type bindings which
        depinject uses to resolve interface inputs to provider functions.  The scope of this
        field's configuration is global (not module specific).
        """
    def __init__(
        self,
        *,
        modules: collections.abc.Iterable[global___ModuleConfig] | None = ...,
        golang_bindings: collections.abc.Iterable[global___GolangBinding] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["golang_bindings", b"golang_bindings", "modules", b"modules"]) -> None: ...

global___Config = Config

@typing_extensions.final
class ModuleConfig(google.protobuf.message.Message):
    """ModuleConfig is a module configuration for an app."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    GOLANG_BINDINGS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """name is the unique name of the module within the app. It should be a name
    that persists between different versions of a module so that modules
    can be smoothly upgraded to new versions.

    For example, for the module cosmos.bank.module.v1.Module, we may chose
    to simply name the module "bank" in the app. When we upgrade to
    cosmos.bank.module.v2.Module, the app-specific name "bank" stays the same
    and the framework knows that the v2 module should receive all the same state
    that the v1 module had. Note: modules should provide info on which versions
    they can migrate from in the ModuleDescriptor.can_migration_from field.
    """
    @property
    def config(self) -> google.protobuf.any_pb2.Any:
        """config is the config object for the module. Module config messages should
        define a ModuleDescriptor using the cosmos.app.v1alpha1.is_module extension.
        """
    @property
    def golang_bindings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GolangBinding]:
        """golang_bindings specifies explicit interface to implementation type bindings which
        depinject uses to resolve interface inputs to provider functions.  The scope of this
        field's configuration is module specific.
        """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        config: google.protobuf.any_pb2.Any | None = ...,
        golang_bindings: collections.abc.Iterable[global___GolangBinding] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "golang_bindings", b"golang_bindings", "name", b"name"]) -> None: ...

global___ModuleConfig = ModuleConfig

@typing_extensions.final
class GolangBinding(google.protobuf.message.Message):
    """GolangBinding is an explicit interface type to implementing type binding for dependency injection."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERFACE_TYPE_FIELD_NUMBER: builtins.int
    IMPLEMENTATION_FIELD_NUMBER: builtins.int
    interface_type: builtins.str
    """interface_type is the interface type which will be bound to a specific implementation type"""
    implementation: builtins.str
    """implementation is the implementing type which will be supplied when an input of type interface is requested"""
    def __init__(
        self,
        *,
        interface_type: builtins.str = ...,
        implementation: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["implementation", b"implementation", "interface_type", b"interface_type"]) -> None: ...

global___GolangBinding = GolangBinding
