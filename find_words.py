if __name__ == '__main__':
    with open('word_list_2.txt') as all_words_raw:
        all_words = all_words_raw.read().split()

    all_words.sort(key = len) # sort word list by length
    print("Number of words = ", len(all_words))

    truncation_chains = []

    for cur_word in all_words:
        if len(cur_word) == 1:
            truncation_chains.append([cur_word])
        else:
            truncation = cur_word[:-1]
            for previous_chain in truncation_chains:
                if previous_chain[-1] == truncation:
                    truncation_chains.append(previous_chain + [cur_word])
                    break

    truncation_chains.sort(key = len, reverse=True)
    if len(truncation_chains) > 0:
        print("Longest found = ", truncation_chains[0])

    output_string = '\n'.join([' > '.join(chain) for chain in truncation_chains])

    with open('sorted_truncation_chains_2.txt', "w") as output_file:
        output_file.write(output_string)
        output_file.close()
