


import random

players_list = []
amalkard = ["name" , "level" , "score" , "status" , "step"]
print("\n\n ***wellcome to my program*** \n\n")
while True :
    print("\n **** MONSTER GAME ****")
    
    amalkard = []
    score = 0

    main_menu = input("\n1.Play game \n2.Top Score \n3.Exit \n")
    match main_menu :
        case "1" :


            player_name = input("please enter your name :\n")
            amalkard.append(player_name)
            print("\nHi" , player_name)
            player_hp = 100
            player_max_hp = 100
            player_max_attack = 20

            player_act = ["punching" , "kick" , "defense" , "potions" , "escape"]
            punching_damge_list = [2 , 4 , 6 , 8 , 10 ]
            kick_damage_list = [4 , 8 , 12 , 16 , 20 ]

            potions_hp = 30
            potions_num = 3
            potions_max_num = 5


            monster_act_list = ["attack" , "defense" , "hard attack"]

            level_list = ["easy","normal","hard"]
            gublin_damage_list = [ 2 , 4 , 6 , 8 , 10]
            gublin_hard_attack = ["theft", 1 , 10 , 5]

            gublin = ["GUBLIN" , 100 , "The Goblin is a sneaky, mischievous creature often found lurking in dark caves and dungeons. Though small, they rely on numbers and cunning to survive. Be careful when exploring their territory—they have 100 HP and can deal a maximum damage of 10 in a single strike!" , gublin_damage_list , gublin_hard_attack ]

            mothman_damage_list = [ 3 , 6 , 9 , 12 , 15]
            mothman_hard_attack = ["shock", 1 , 15 , 5]

            mothman = ["MOTHMAN" , 150 ,"The Mothman is a legendary, winged cryptid shrouded in mystery and omen, often spotted hovering near shadowed bridges or dark woods. With piercing glowing red eyes, it strikes fear into any traveler foolish enough to disturb it. It possesses 150 HP and can deal a maximum damage of 15 in a single terrifying swoop!" , mothman_damage_list , mothman_hard_attack]

            leshy_damage_list = [ 4 , 8 , 12 , 16 , 20]
            leshy_hard_attack = ["potion", 1 , 20 , 10]

            leshy = ["LESHY" , 200 , "The Leshy is an ancient, powerful spirit of the forest, embodying the wild and untamed nature of the woods. Often appearing as a tall, humanoid figure with bark-like skin and mossy hair, it protects its domain fiercely. Woe betide those who disrespect the forest, for the Leshy has 200 HP and can deliver a crushing blow of up to 20!" , leshy_damage_list , leshy_hard_attack]

            dragon_damage_list = [ 5 , 10 , 15 , 20 , 25]
            dragon_hard_attack = ["fire", 1 , 25 , 10]

            dragon = ["DRAGON" , 250 , "The Dragon is a mighty, fire-breathing creature with shining scales and powerful wings. It guards its treasure fiercely and can unleash a devastating attack. It has 250 HP and can deal up to 25 damage with a single strike." , dragon_damage_list , dragon_hard_attack]



            monster_list = [gublin , mothman , leshy , dragon]

            k = 0
            j = 0
            while True :
                
                player_hp = 100
                

                if k == 1 or j ==1:
                    break

                level = input("\nchoise LEVEL :\n1.easy \n2.normal \n3.hard\n4.Exit\n")

                match level :
                    case "1" :
                        monster_wheight = [30 , 25 , 20 , 15 , 10]
                        monster_act_wheight = [6 , 3 , 1]
                        player_wheight = [10 , 15 , 20 , 25 , 30]
                        level_name = "easy"
                        zarib_score = 1
                    case "2" :
                        monster_wheight = [20 , 20 , 20 , 20 , 20]
                        monster_act_wheight = [4 , 4 , 2]
                        player_wheight = [20 , 20 , 20 , 20 , 20]
                        level_name = "normal"
                        zarib_score = 2
                    case "3" :
                        monster_wheight = [10 , 15 , 20 , 25 , 30]
                        monster_act_wheight = [3 , 5 , 2]
                        player_wheight = [30 , 25 , 20 , 15 , 10]
                        level_name = "hard"
                        zarib_score = 3
                    case _ :
                        break

                amalkard.append(level_name)
                i = 0
                

                for monster in monster_list :

                    if j == 1 :
                        break

                    i +=1

                    monster_name = monster[0]
                    monster_hp = monster[1]
                    monster_max_hp = monster[1]
                    monster_detail = monster[2]
                    monster_damage_list = monster[3]
                    monster_hard_attack = monster[4]

                    print("\nlevel :" , level_name , "STEP" , i , " : " , monster_name )
                    print( monster_detail)
                    print()

                    if player_hp > 0 :
                        while True :
                            print(player_name , "  helth : " , player_hp ,"/", player_max_hp , "  potions : " , potions_num)
                            print(monster_name , " health :" , monster_hp , "/" , monster_max_hp)
                            player_act_choise = input("\nchoice yout act :\n1.punching \n2.kicking \n3.defensing \n4.eat potions \n5.escape\n")
                            match player_act_choise :
                                case "1" :
                                    player_damage = random.choices(punching_damge_list , weights = player_wheight )[0]
                                    print("PUNCH.....!!!!")
                                    print("your damage is" , player_damage)
                                    monster_act_choise = random.choices(monster_act_list , weights = monster_act_wheight)[0]
                                    if monster_act_choise == "defense" :
                                        print(" but oohhh the monster defended itself")

                                    elif monster_act_choise == "attack" :
                                        monster_damage = random.choices(monster_damage_list , weights = monster_wheight )[0]
                                        print (monster_name , "has attack to you by " , monster_damage , " damage")
                                        player_hp = player_hp - monster_damage
                                        monster_hp -= player_damage
                                        score += player_damage * zarib_score
                                        if player_hp <= 0 :
                                            print("YOU ARE DEAD")
                                            amalkard.append(score)
                                            amalkard.append("DIE")
                                            amalkard.append(monster_name)
                                            players_list.append(amalkard)
                                            break
                                        elif monster_hp <= 0 :
                                            print("YOU ARE WIN \n YOU KILL" , monster_name)
                                            if i == 4 :
                                                amalkard.append(score)
                                                amalkard.append("WIN")
                                                amalkard.append(monster_name)
                                                players_list.append(amalkard)
                                                print("WOOOOOWWW YOU ARE AMAZING YOU KILL DRAGOOOOOOOOOOOOONNNN")
                                            if potions_num < potions_max_num :
                                                potions_num +=1
                                                player_hp += 25 * i
                                                if player_hp > player_max_hp :
                                                    player_hp = player_max_hp
                                            
                                            break
                                        else :
                                            continue
                                    elif monster_act_choise == "hard attack" :
                                        
                                        if monster_hard_attack[1] > 0 :

                                            print("ooohhh my god " , monster_name , "has HARD ATTACKKKKK" , monster_hard_attack[0] )

                                            player_hp -= monster_hard_attack[2]
                                            if player_hp <= 0 :
                                                print("YOU ARE DEAD")
                                                amalkard.append(score)
                                                amalkard.append("DIE")
                                                amalkard.append(monster_name)
                                                players_list.append(amalkard)
                                                break
                                            monster_hp += monster_hard_attack[3]
                                            if monster_hp > monster_max_hp :
                                                monster_hp = monster_max_hp

                                            monster_hard_attack[1] -= 1
                                        else :
                                            monster_hp -= player_damage
                                            score += player_damage * zarib_score
                                            if monster_hp <= 0 :
                                                print("YOU ARE WIN \n YOU KILL" , monster_name)
                                                if i == 4 :
                                                    amalkard.append(score)
                                                    amalkard.append("WIN")
                                                    amalkard.append(monster_name)
                                                    players_list.append(amalkard)
                                                    print("WOOOOOWWW YOU ARE AMAZING YOU KILL DRAGOOOOOOOOOOOOONNNN")
                                                if potions_num < potions_max_num :
                                                    potions_num +=1
                                                    player_hp += 25 * i
                                                    if player_hp > player_max_hp :
                                                        player_hp = player_max_hp
                                                
                                                break
                                case "2" :
                                    
                                    player_damage = random.choices(kick_damage_list , weights = player_wheight )[0]
                                    print("KICK.....!!!!")
                                    player_hp -= i
                                    print("your damage is" , player_damage , "and your health" , i , "is low becouse you use kick")
                                    monster_act_choise = random.choices(monster_act_list , weights = monster_act_wheight)[0]
                                    if monster_act_choise == "defense" :
                                        print("oohhh the monster defended itself")

                                    elif monster_act_choise == "attack" :
                                        monster_damage = random.choices(monster_damage_list , weights = monster_wheight )[0]
                                        print (monster_name , "has attack to you by " , monster_damage , " damage")
                                        player_hp = player_hp - monster_damage
                                        monster_hp -= player_damage
                                        score += player_damage * zarib_score
                                        if player_hp <= 0 :
                                            print("YOU ARE DEAD")
                                            amalkard.append(score)
                                            amalkard.append("DIE")
                                            amalkard.append(monster_name)
                                            players_list.append(amalkard)
                                            break
                                        elif monster_hp <= 0 :
                                            print("YOU ARE WIN \n YOU KILL" , monster_name)
                                            if i == 4 :
                                                amalkard.append(score)
                                                amalkard.append("WIN")
                                                amalkard.append(monster_name)
                                                players_list.append(amalkard)
                                                print("WOOOOOWWW YOU ARE AMAZING YOU KILL DRAGOOOOOOOOOOOOONNNN")
                                                
                                            if potions_num < potions_max_num :
                                                potions_num +=1
                                                player_hp += 25 * i
                                                if player_hp > player_max_hp :
                                                    player_hp = player_max_hp
                                            
                                            break
                                        else :
                                            continue
                                    elif monster_act_choise == "hard attack" :
                                        
                                        if monster_hard_attack[1] > 0 :

                                            print("ooohhh my god " , monster_name , "has HARD ATTACKKKKK" , monster_hard_attack[0] )

                                            player_hp -= monster_hard_attack[2]

                                            monster_hp += monster_hard_attack[3]
                                            if monster_hp > monster_max_hp :
                                                monster_hp = monster_max_hp

                                            monster_hard_attack[1] -= 1
                                            if player_hp <= 0 :
                                                print("YOU ARE DEAD")
                                                amalkard.append(score)
                                                amalkard.append("DIE")
                                                amalkard.append(monster_name)
                                                players_list.append(amalkard)
                                                break
                                        else :
                                            monster_hp -= player_damage
                                            score += player_damage * zarib_score
                                            if monster_hp <= 0 :
                                                print("YOU ARE WIN \n YOU KILL" , monster_name)
                                                if i == 4 :
                                                    amalkard.append(score)
                                                    amalkard.append("WIN")
                                                    amalkard.append(monster_name)
                                                    players_list.append(amalkard)
                                                    print("WOOOOOWWW YOU ARE AMAZING YOU KILL DRAGOOOOOOOOOOOOONNNN")
                                                if potions_num < potions_max_num :
                                                    potions_num +=1
                                                    player_hp += 25 * i
                                                    if player_hp > player_max_hp :
                                                        player_hp = player_max_hp
                                                
                                                break

                                case "3" :
                                    print("defense")
                                    score += i * zarib_score
                                    player_hp -= i*2

                                    monster_act_choise = random.choices(monster_act_list , weights = monster_act_wheight)[0]
                                    if monster_act_choise == "hard attack" :
                                        
                                        if monster_hard_attack[1] > 0 :

                                            print("ooohhh my god " , monster_name , "has HARD ATTACKKKKK" , monster_hard_attack[0] )

                                            monster_hp += monster_hard_attack[3]
                                            if monster_hp > monster_max_hp :
                                                monster_hp = monster_max_hp

                                            monster_hard_attack[1] -= 1
                                        
                                    else :
                                        continue
                                case "4" :
                                    print("you eating potions and your health 30 up")
                                    if potions_num > 0 :
                                        potions_num -=1
                                        player_hp += 30
                                        score -= 5  * zarib_score
                                        if player_hp > player_max_hp :
                                            player_hp = player_max_hp
                                    else :
                                        print("you dont have potions")
                                
                                case "5" :
                                    j = 1
                                    score -= int(100  / zarib_score)
                                    amalkard.append(score)
                                    amalkard.append("escape")
                                    amalkard.append(monster_name)
                                    players_list.append(amalkard)
                                    print("toooffffffffffff")
                                    break
                                case _ :
                                    continue
                    else :
                        k = 1
                        print("you are dieeeee")    
                        break
        case "2" :
            print(players_list)
        case _ :
            print("goodbye")
            break
    
            





