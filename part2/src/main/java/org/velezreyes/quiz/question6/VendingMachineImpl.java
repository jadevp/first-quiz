package org.velezreyes.quiz.question6;

// Clase abstracta para una bebida genérica
abstract class AbstractDrink implements Drink {
  private String name;
  private boolean isFizzy;
  private int cost;

  public AbstractDrink(String name, boolean isFizzy, int cost) {
    this.name = name;
    this.isFizzy = isFizzy;
    this.cost = cost;
  }

  public String getName() { return name; }
  public boolean isFizzy() { return isFizzy; }
  public int getCost() { return cost; }
}

// Clase para la bebida "ScottCola"
class ScottCola extends AbstractDrink {
  public ScottCola() {
    super("ScottCola", true, 3);
  }
}

// Clase para la bebida "KarenTea"
class KarenTea extends AbstractDrink {
  public KarenTea() {
    super("KarenTea", false, 4);
  }
}

public class VendingMachineImpl implements VendingMachine {
  private int quarters = 0;
  private static VendingMachineImpl instance = null;

  private VendingMachineImpl() {}

  public static VendingMachine getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  public void insertQuarter() {
    quarters++;
  }

  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    AbstractDrink drink;

    switch (name) {
      case "ScottCola":
        drink = new ScottCola();
        break;
      case "KarenTea":
        drink = new KarenTea();
        break;
      default:
        throw new UnknownDrinkException();
    }

    if (quarters < drink.getCost()) {
      throw new NotEnoughMoneyException();
    }

    quarters -= drink.getCost();

    return drink;
  }
}