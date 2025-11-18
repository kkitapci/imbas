import math

# This program calculates Speech Transmission Index (STI) 
# as a function of Reverberation Time (RT) and Signal-to-Ratio

# The modulation frequencies are defined in the below given list. DO NOT CHANGE!
MODULATION_FREQUENCIES = [0.63, 0.8, 1.0, 1.25, 1.6, 2.0, 2.5, 3.15, 4.0, 5.0, 6.3, 8.0, 10.0, 12.5]

# The octave band frequencies are defined in the below given dictionary, alongside empirical weighting factors.
# as in -> frequency: weighting. DO NOT CHANGE!

OCTAVE_BAND_FREQUENCIES = {
    125: 0.13,
    250: 0.14,
    500: 0.11,
    1000: 0.12,
    2000: 0.19,
    4000: 0.17,
    8000: 0.14
}

# User defined destructors are the Reverberation Time (RT) and the Signal-to-Noise Ratio (RT).
# as in -> frequency: [reverberation, signal-to-noise]
user_defined_destructors = {
    125: [1, 5],
    250: [1, 5],
    500: [1, 5],
    1000: [1, 5],
    2000: [1, 5],
    4000: [1, 5],
    8000: [1, 5]
}

# This function calculates the Modulation Transfer Factor.

def calculate_modulation_transfer_factor(modulation_frequency: int, reverberation_time: float, snr: float) -> float:
    reverberation_component = 1 / (math.sqrt(1 + math.pow((2 * math.pi * modulation_frequency * reverberation_time / 13.8), 2)))
    noise_component = 1 / (1 + math.pow(10, (-0.1 * snr)))
    modulation_transfer_factor = reverberation_component * noise_component
    return modulation_transfer_factor

# This function calculates the Apparent Signal-to-Noise ratio.

def calculate_lsnapp(modulation_frequency: int) -> float:
    lsnapp = 10 * math.log10 (modulation_frequency / (1 - modulation_frequency))
    return lsnapp

# This function calculated the Speech Transmission Index (STI).

def calculate_sti(cumulative_lsnapp: float) -> float:
    sti = (cumulative_lsnapp + 15) / 30
    return sti

def main():
    temp_lsnapp = {
    125: [],
    250: [],
    500: [],
    1000: [],
    2000: [],
    4000: [],
    8000: []
    }

    average_lsnapp = {
    125: 0.0,
    250: 0.0,
    500: 0.0,
    1000: 0.0,
    2000: 0.0,
    4000: 0.0,
    8000: 0.0
    }

    for frequency in list(temp_lsnapp.keys()):
        for modulation_frequency in MODULATION_FREQUENCIES:
            rt, snr = user_defined_destructors[frequency]
            lsnapp = calculate_modulation_transfer_factor(modulation_frequency, rt, snr)
            temp_lsnapp[frequency].append(lsnapp)

    for frequency in list(average_lsnapp.keys()):
        average_lsnapp[frequency] = sum(temp_lsnapp[frequency]) / len(temp_lsnapp[frequency])
        average_lsnapp[frequency] = calculate_lsnapp(average_lsnapp[frequency]) * OCTAVE_BAND_FREQUENCIES[frequency]

    cumulative_lsnapp = sum(list(average_lsnapp.values()))

    sti = calculate_sti(cumulative_lsnapp)

    print(f"STI = {sti:.2f}")

# The main function starts.
main()