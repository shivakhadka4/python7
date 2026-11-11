from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())


def test_battle(first: CreatureFactory, second: CreatureFactory) -> None:
    print("Testing battle")
    fighter_one = first.create_base()
    fighter_two = second.create_base()
    print(fighter_one.describe())
    print(" vs.")
    print(fighter_two.describe())
    print(" fight!")
    print(fighter_one.attack())
    print(fighter_two.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
