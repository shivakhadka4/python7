from ex0 import Creature
from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def test_healer(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())


def test_transformer(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    print("Testing Creature with healing capability")
    print(" base:")
    test_healer(healing_factory.create_base())
    print(" evolved:")
    test_healer(healing_factory.create_evolved())
    print()
    transform_factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")
    print(" base:")
    test_transformer(transform_factory.create_base())
    print(" evolved:")
    test_transformer(transform_factory.create_evolved())


if __name__ == "__main__":
    main()
