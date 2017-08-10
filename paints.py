class paint():
    def paint(self, make, coverage, price, litres):
        self.make = make
        self.coverage = coverage
        self.price = price
        self.litres = litres

        def getTotalCoverage(litres, coverage):
            return litres*coverage

        def getTotalPrice(getTotalCoverage, price):
            return getTotalCoverage*price

        def getCoverage(coverage):
            return coverage