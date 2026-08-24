class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            while stack and asteroid < 0 and stack[-1] > 0:

                # Stack asteroid is smaller
                if stack[-1] < abs(asteroid):
                    stack.pop()

                # Both are same size
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    break

                # Stack asteroid is bigger
                else:
                    break

            else:
                stack.append(asteroid)

        return stack