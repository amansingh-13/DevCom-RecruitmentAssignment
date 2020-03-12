The implementation of ranking events can be understood by prioritizer.py [here](https://github.com/wncc/IITBapp/tree/master/events)  <br />

```python
BASE = 1000                              # Base points
FINISHED_PENALTY = 600                   # Direct penalty if event is done
WEIGHT_START_TIME = 800                  # Weight of time from event start
WEIGHT_END_TIME = 800                    # Weight of time from event end
TIME_SD = 2.5                            # Standard deviation of time distribution
TIME_L_END = 1.2                         # Lambda for exponential of ended penalty
BODY_FOLLOWING_BONUS = 100               # Bonus if the body is followed
TIME_DEP_BODY_BONUS = 200                # Bonus if the body is followed dependent on time
BODY_BONUS_MAX = 400                     # Maximum bonus for followed bodies
TIME_PENALTY_FACTOR = 0.05               # Multiplying factor for event length penalty
LINEAR_DECAY = 0.05                      # Slope of linear decay
FAR_OFF_THRESHOLD = 15                   # Time in days after which events are considered far off
NOT_TAG_TARGET_PENALTY = 2000            # Penalty if not targeted in a restricted even
```
This is calculation is used to order events.<br />
For our application, we can do something on the same lines, like this:

```python
BASE = 1000                              # Base points
WEIGHT_START_TIME = -200                 # Weight of time from which the book is up for lending, negative as want
                                         # older books to be lent  first 
GENRE_FOLLOWING_BONUS = 500              # Bonus if the genre is followed
CLOSENESS_BONUS = 100                    # Bonus if lender lives near
BRANCH_EXACTNESS BONUS = 400             # Bonus if branch is same, will help in lending of course material
```
