import random


def state(State_name,electoral_college,trump_odds,biden_odds):
    a =random.choices(
        population = [['Trump', 'Biden'],['Biden', 'Trump']],
                      weights = [trump_odds,biden_odds],k =1)
    #print(a[0][0]+ f" wins {State_name}")
    return a[0][0]

def main():
    for i in range(0,10): 
        Biden_wins = 0
        Trump_wins = 0
        number_of_sims = 1000
        for i in range(0,number_of_sims):
            
            Biden = 0
            Trump = 0
            state_name = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                          "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                          "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachussets", "Michigan", "Minnesota", "Mississippi", "Missouri",
                          "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
                          "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
                          "Washington", "West Virginia", "Wisconsin", "Wyoming"]
            elec_votes = [9,3,11,6,55,9, 7, 3, 3,29,16,4,4,
                          20,11,6,6,8,8,4,10,11,16,10,6,10,3,5,6,
                          4,14,5,29,15,
                          3,18,7,7,20,4,9,3,11,38,6,3,13,12,5,10,3]

            trump_odds = [0.98,0.85,0.32,0.99,0.01,0.03,0.01,0.01,0.01,
                          0.31,0.42,0.01,0.99,0.01,0.96,0.61,0.98,0.98,
                          0.98,0.10,0.01,0.01,0.05,0.04,0.92,0.93,0.84,0.99,
                          0.12,0.11,0.01,0.02,0.01,0.35,0.98,0.54,0.99,
                          0.02,0.15,0.01,0.91,0.95,0.97,0.61,0.95,0.01,
                          0.01,0.01,0.99,0.06,0.99]

            
            
           
            for i in range(len(state_name)):
                winner = state(state_name[i],elec_votes[i],trump_odds[i],1-trump_odds[i])
                if winner == "Trump":
                    Trump += elec_votes[i]
                else:
                    Biden += elec_votes[i]
            if Biden >= Trump:
                Biden_wins +=1
            else:
                Trump_wins +=1

        print(f"After {number_of_sims} simulations, Joe Biden wins {Biden_wins} times and Trump wins {Trump_wins} times")
              

if __name__ == '__main__':
    main()
