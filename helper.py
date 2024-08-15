import numpy as np
import pandas as pd

## Parsed bitstrings
def adder_truth_table(adder_counts):
    bits = []
    for count in adder_counts:
        bitstring_arr = []
        for char in count:
            for i in char:
                bitstring_arr.append(i)
        bits.append(bitstring_arr)


    ## Probability distribution
    probs = []

    for count in adder_counts:
        probs.append(adder_counts[count])

    norm_factor = np.sqrt(np.sum(np.square(probs)))
    probs /= norm_factor
    probs = np.square(probs)

    df = pd.DataFrame(np.transpose([[int(bits[i][4]) for i in reversed(range(8))],
                                    [int(bits[i][3]) for i in reversed(range(8))],
                                    [int(bits[i][2]) for i in reversed(range(8))],
                                    [int(bits[i][0]) for i in reversed(range(8))],
                                    [int(bits[i][1]) for i in reversed(range(8))],
                                    [probs[i] for i in reversed(range(8))]]),
                        columns=['a', 'b', 'cin', 'cout', 'sum', 'probability']
                     )

    s = df.style.hide(axis = 'index').format(precision=0,
                    formatter={('a', 'b', 'cin', 'cout', 'sum'): "{:.2f}",
                               ('probability'): "{:.3f}",
                              })
    s.set_table_styles(
        [{"selector": "", "props": [("border", "1px solid grey")]},
          {"selector": "tbody td", "props": [("border", "1px solid grey")]},
         {"selector": "th", "props": [("border", "1px solid grey")]}
        ]
    )
    display(s)