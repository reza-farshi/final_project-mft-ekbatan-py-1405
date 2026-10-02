


main_list = []
name_list = []
serial_list = []
brand_list = []
kahesh_list = []
afzayesh_list = []

last_serial_elc = 10001110
last_serial_lavazem = 20001110
last_serial_pooshak = 30001110
last_serial_ghataat = 40001110
last_serial_other = 50001110

ex = 0
exx = 0

while True :
    if ex == 1 :
        break
    
    while True :
        if ex == 1 :
            break

        m = input("1.vorode kala \n2.moshahede kala\n3.exit\n")
        exx = 0
        match m :
            case "1" :
                kala = []
                shakhe_kala = []
                noe_kala = []
                kala_brand = []
                kala_serial = []
                kala_name = []
                kala_num = []
                kala_price = []
                kala = [ kala_serial , shakhe_kala , kala_brand , kala_name , kala_num , kala_price , noe_kala]

                shakhe_kala_ent = input("shakhe kala ra vared koni :\n1.electronic \n2.lavazem khanegi \n3.pooshak \n4.ghataate khodro \n5.other \n6.back \n")
                match shakhe_kala_ent :
                    case "1" :
                        shakhe_kala_ent = "electronic"
                        noe_kala_ent = input("\nlotfan noe kala ra vared konid : \n1.mobile \n2.laptop \n3.tablet \n4.other\n")
                        match noe_kala_ent :
                            case "1" :
                                noe_kala_ent = "mobile"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.apple \n2.samsong \n3.xiaomi \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "apple"
                                    case "2" :
                                        kala_brand_ent = "samsong"
                                    case "3" :
                                        kala_brand_ent = "xiaomi"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "2" :
                                noe_kala_ent = "laptop"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.apple \n2.asus \n3.lenovo \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "apple"
                                    case "2" :
                                        kala_brand_ent = "asus"
                                    case "3" :
                                        kala_brand_ent = "lenovo"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "3" :
                                noe_kala_ent = "tablet"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.apple \n2.samsong \n3.xiaomi \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "apple"
                                    case "2" :
                                        kala_brand_ent = "samsong"
                                    case "3" :
                                        kala_brand_ent = "xiaomi"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "4" :
                                noe_kala_ent = input("lotfan noe kalaye morede nazare khod ra vared konid :\n")
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                            case _ :
                                break

                    case "2" :
                        shakhe_kala_ent = "lavazem khanegi"
                        noe_kala_ent = input("\nlotfan noe kala ra vared konid : \n1.tv \n2.yakhchal \n3.jaroo barghi \n4.other\n")
                        match noe_kala_ent :
                            case "1" :
                                noe_kala_ent = "tv"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.LG \n2.samsong \n3.deawoo \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "LG"
                                    case "2" :
                                        kala_brand_ent = "samsong"
                                    case "3" :
                                        kala_brand_ent = "deawoo"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "2" :
                                noe_kala_ent = "yakhchal"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.LG \n2.samsong \n3.deawoo \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "LG"
                                    case "2" :
                                        kala_brand_ent = "samsong"
                                    case "3" :
                                        kala_brand_ent = "deawoo"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "3" :
                                noe_kala_ent = "jaroo barghi"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.bousch \n2.LG \n3.pars khazar \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "bousch"
                                    case "2" :
                                        kala_brand_ent = "LG"
                                    case "3" :
                                        kala_brand_ent = "pars khazar"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "4" :
                                noe_kala_ent = input("lotfan noe kalaye morede nazare khod ra vared konid :\n")
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                            case _ :
                                break

                    case "3" :
                        shakhe_kala_ent = "pooshak"
                        noe_kala_ent = input("\nlotfan noe kala ra vared konid : \n1.shalvar \n2.pirahan \n3.kafsh \n4.other\n")
                        match noe_kala_ent :
                            case "1" :
                                noe_kala_ent = "shalvar"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.jeen \n2.katan \n3.parche \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "jeen"
                                    case "2" :
                                        kala_brand_ent = "katan"
                                    case "3" :
                                        kala_brand_ent = "parche"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "2" :
                                noe_kala_ent = "pirahan"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.t-shert \n2.majlesi \n3.sport \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "t-shert"
                                    case "2" :
                                        kala_brand_ent = "majlesi"
                                    case "3" :
                                        kala_brand_ent = "sport"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "3" :
                                noe_kala_ent = "kafsh"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.salamon \n2.nike \n3.adidas \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "salamon"
                                    case "2" :
                                        kala_brand_ent = "nike"
                                    case "3" :
                                        kala_brand_ent = "adidas"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "4" :
                                noe_kala_ent = input("lotfan noe kalaye morede nazare khod ra vared konid :\n")
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                            case _ :
                                break

                    case "4" :
                        shakhe_kala_ent = "ghataate khodro"
                        noe_kala_ent = input("\nlotfan noe kala ra vared konid : \n1.motor \n2.gearbox \n3.badane \n4.other\n")
                        match noe_kala_ent :
                            case "1" :
                                noe_kala_ent = "motor"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.iran khodro \n2.saipa \n3.hyundai-kia \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "iran khodro"
                                    case "2" :
                                        kala_brand_ent = "saipa"
                                    case "3" :
                                        kala_brand_ent = "hyundai-kia"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "2" :
                                noe_kala_ent = "gearbox"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.iran khodro \n2.saipa \n3.hyundai-kia \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "iran khodro"
                                    case "2" :
                                        kala_brand_ent = "saipa"
                                    case "3" :
                                        kala_brand_ent = "hyundai-kia"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "3" :
                                noe_kala_ent = "badane"
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n1.iran khodro \n2.saipa \n3.hyundai-kia \n4.other \n")
                                match kala_brand_ent :
                                    case "1" :
                                        kala_brand_ent = "iran khodro"
                                    case "2" :
                                        kala_brand_ent = "saipa"
                                    case "3" :
                                        kala_brand_ent = "hyundai-kia"
                                    case "4" :
                                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                                    case _ :
                                        break
                            case "4" :
                                noe_kala_ent = input("lotfan noe kalaye morede nazare khod ra vared konid :\n")
                                kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                            case _ :
                                break
                        
                    case "5" :
                        shakhe_kala_ent = input("lotfan shakhe kala morede nazar ra vared konid : \n")
                        noe_kala_ent = input("lotfan noe kalaye morede nazare khod ra vared konid :\n")
                        kala_brand_ent = input("lotfan brande morede nazare khod ra vared konid :\n")
                    case _ :
                        break

                
                
                kala_name_ent = input("name kala ra vared koni :\n")
                x = 0
                y = 0
                for i in name_list :
                    if i == kala_name_ent  :
                        print("kala az ghabl mojod ast")
                        print(main_list[x])
                        y +=1
                    x += 1
                if y > 0 :
                    menu = input("1.kalaye jadid ast \n2.kala tekrari ast \n")
                    match menu :
                        case "1" :
                            kala_name.append(kala_name_ent)
                            name_list.append(kala_name_ent)
                            
                        case "2" :
                            break
                else :
                    kala_name.append(kala_name_ent)
                    name_list.append(kala_name_ent)
                    
                shakhe_kala.append(shakhe_kala_ent)
                
                noe_kala.append(noe_kala_ent)

                kala_brand.append(kala_brand_ent)
                brand_list.append(kala_brand_ent)

                kala_num_ent = input("tedade kala ra vared koni :\n")
                kala_num.append(kala_num_ent)

                kala_price_ent = input("gheymat kala ra vared koni :\n")
                kala_price.append(kala_price_ent)

                if shakhe_kala_ent == "electronic" :

                    serial = last_serial_elc + 1
                    last_serial_elc = serial
                    kala_serial.append(serial)
                    serial_list.append(serial)
                elif shakhe_kala_ent == "lavazem khanegi" :
                
                    serial = last_serial_lavazem + 1
                    last_serial_lavazem = serial
                    kala_serial.append(serial)
                    serial_list.append(serial)
                elif shakhe_kala_ent == "pooshak" :
                                
                    serial = last_serial_pooshak + 1
                    last_serial_pooshak = serial
                    kala_serial.append(serial)
                    serial_list.append(serial)
                elif shakhe_kala_ent == "ghataate khodro" :
                                
                    serial = last_serial_ghataat + 1
                    last_serial_ghataat = serial
                    kala_serial.append(serial)
                    serial_list.append(serial)
                else :
                                
                    serial = last_serial_other + 1
                    last_serial_other = serial
                    kala_serial.append(serial)
                    serial_list.append(serial)

                main_list.append(kala)

            case "2" :
                while True :

                    if exx == 1 :
                        break

                    main_menu = input("\n1.moshahede mojodi kol \n2.search mahsool \n3.exit \n")
                    while True :

                        
                        match main_menu :
                            case "1" :  
                                menu = input("1.mojodi bar asase brand \n2.mojodi kol \n3.liste afzayesh \n4.liste kahesh \n5.back \n ")
                                match menu :
                                    case "1" :
                                        search = input("lotfan brande morde nazare khod ra vared namayid :\n")
                                        x = 0
                                        num = 0
                                        for i in brand_list :
                                            if i == search :
                                                
                                                print(main_list[x])
                                                num += 1

                                            x += 1
                                        if num == 0 :
                                            print("brande morede nazar peyda nashod")
                                            
                                    case "2" :
                                        print(main_list)  
                                    case "3" :
                                        print(afzayesh_list)
                                    case "4" :
                                        print(kahesh_list)
                                    case _ :
                                        break
                                break

                            case "2" :

                                search = input("please enter name or serial number :\n")

                                if search.isdigit() :

                                    search = int(search)
                                z = 0
                                num = 0
                                for i in name_list :
                                    if i == search  :
                                        print(main_list[z])
                                        x = z
                                        num += 1
                                    z +=1
                                if num > 1 :
                                    print("lotfan ba shomare serial jostojoo konid")
                                    break
                                if num == 0 :
                                    
                                    if search in serial_list :
                                        x = serial_list.index(search)
                                        print(main_list[x])
                                    
                                    if search not in serial_list  :
                                        print("kalaye morede nazar peyda nashod")
                                        break

                                menu = input("\n1.taghire gheymat \n2.afzayesh mojodi \n3.kahesh mojodi \n4.hazf \n5.back \n")
                                
                                match menu :
                                    case "1" :
                                        print("gheymate feeli :" , main_list[x][5][0])
                                        new_price = input("lotfan gheymate jadid ra vared namayid :\n")
                                        main_list[x][5][0] = new_price
                                        break
                                    case "2" :
                                        print("mojoodie feeli : " , main_list[x][4][0])
                                        up_num = int(input("lotfan tedade afzayeshe mojodi ra vared namayid :\n"))
                                        old_num = int(main_list[x][4][0])
                                        new_num = old_num + up_num
                                        main_list[x][4][0] = new_num
                                        afzayesh = []
                                        afzayesh.append(main_list[x][0])
                                        afzayesh.append(main_list[x][1])
                                        afzayesh.append(main_list[x][2])
                                        afzayesh.append(main_list[x][3])
                                        afzayesh.append(up_num)
                                        afzayesh.append(main_list[x][5])
                                        afzayesh.append(main_list[x][6])

                                        afzayesh_list.append(afzayesh)

                                        break
                                    case "3" :
                                        print("mojoodie feeli : " , main_list[x][4][0])
                                        low_num = int(input("lotfan tedade afzayeshe mojodi ra vared namayid :\n"))
                                        old_num = int(main_list[x][4][0])
                                        new_num = old_num - low_num
                                        main_list[x][4][0] = new_num
                                        kahesh = []
                                        kahesh.append(main_list[x][0])
                                        kahesh.append(main_list[x][1])
                                        kahesh.append(main_list[x][2])
                                        kahesh.append(main_list[x][3])
                                        kahesh.append(up_num)
                                        kahesh.append(main_list[x][5])
                                        kahesh.append(main_list[x][6])

                                        kahesh_list.append(kahesh)

                                        if new_num < 5 :
                                            print("mojodie kala be nahie khatar nazdik shode ast")
                                        break
                                    case "4" :
                                        main_list.remove(main_list[x])
                                        name_list.remove(name_list[x])
                                        serial_list.remove(serial_list[x])
                                        brand_list.remove(brand_list[x])
                                        break
                                    case _ :
                                        break
                                break
                            case _ :
                                exx = 1
                                break
                    
            case "3" :
                ex = 1
                break
            case _ :
                continue


