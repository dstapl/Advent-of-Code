class Report:
    def __init__(self, report: list[int]):
        self.length = len(report)
        self.report = report

    def isSafe(self) -> tuple[bool, int]:
        """
        Adjacent levels *must* be all strictly increasing *or* decreasing
        Differences must be at least 1 (>=) and at most 3 (<=)

        Returns safe(bool) and index of unsafe (idx or -1 for Safe)
        """

        prev, curr = self.report[0], self.report[1]
        # (Decreasing, Same, increasing) = (-1,0,1)
        prev_direction, _ = Report.direction(prev,curr)  
        if not Report.adjacentSafe(prev, curr, prev_direction):
            return (False,1)

        for i in range(2, len(self.report)):
            prev = curr
            curr = self.report[i]
            if not Report.adjacentSafe(prev, curr, prev_direction):
                return (False, i)

        return (True, -1)
 
    def reallySafe(self) -> bool:
        if self.isSafe()[0]:
            return True
        for i in range(self.length):
            old_report = self.report[:]
            self.report = self.report[:i] + self.report[i+1:] 

            if self.isSafe()[0]:
                return True
            # Restore old report
            self.report = old_report
        return False
 
    @staticmethod
    def adjacentSafe(prev:int, curr:int, prev_direction):
        curr_direction, diff = Report.direction(prev,curr)

        if (curr_direction == 0) or (curr_direction != prev_direction):
            return False

        # diff == 0 checked inside direction
        if not (1 <= abs(diff) <= 3):
            return False

        return True

    @staticmethod
    def difference(prev:int, curr:int):
        return curr - prev

    @staticmethod
    def direction(prev: int, curr: int):
        diff = Report.difference(prev,curr)
        if diff > 0:
            direction = 1
        elif diff == 0:
            direction = 0
        else:
            direction = -1
        return [direction, diff]

    def __repr__(self):
        return f"{self.report = };{'Safe' if self.isSafe() else 'Unsafe'}"

def parse_file(file):
    reports = map(lambda x: list(map(lambda y: int(y.strip()), x)), map(lambda s: s.split(" "), file))
    reports_parsed = map(Report, reports)
    return list(reports_parsed) 


def main():
    file = open(0).readlines()
    reports = parse_file(file)
    safe = list(map(Report.isSafe, reports))
    print("Part 1: ", sum(map(lambda x: x[0],safe)))

    safe_removeone = list(map(Report.reallySafe, reports))
    print("Part 2: ", sum(safe_removeone))

if __name__ == "__main__":
    main()
