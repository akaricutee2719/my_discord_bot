answers = ""
class money_banana:
    def chuyen_tien(tag,tag_given, money):
        
        money_in_txt = open(f'assets\\information_id\\{tag}.txt')
        money_left= money_in_txt.read()
        if int(money) > int(money_left):
            answers = "bạn không có đủ banana để chuyển !"
        elif int(money) <= 0:
            answers ="giá trị không đúng !"
        elif not money.isdigit():
            answers ="giá trị không đúng !"
        elif int(money) > 10000000000000:
            if str(tag) != '748439531761434676':
                answers = "mỗi lần chuyển chỉ được tiêu ít hơn 100000 :banana: !"
            else:
                if str(tag_given) == '748439531761434676':
                    money_give_in_txt = open(f'assets\\information_id\\{tag_given}.txt','r')
                    money_in_txt_2 = open(f'assets\\information_id\\{tag}.txt','w')
                    money_given = int(money_give_in_txt.read())
                    money_give_in_txt_2 = open(f'assets\\information_id\\{tag_given}.txt','w')
                    money_left_after = int(money_left) - int(money)
                    money_given = money_given + int(money)
                    answers = f"bạn đã chuyển thành công số banana là **{int(money):,d}** :banana: !"
                    money_in_txt_2.write(str(money_left_after))
                    money_give_in_txt_2.write(str(money_given))
        else:
            money_give_in_txt = open(f'assets\\information_id\\{tag_given}.txt','r')
            money_in_txt_2 = open(f'assets\\information_id\\{tag}.txt','w')
            money_given = int(money_give_in_txt.read())
            money_give_in_txt_2 = open(f'assets\\information_id\\{tag_given}.txt','w')
            money_left_after = int(money_left) - int(money)
            money_given = money_given + int(money)
            answers = f"bạn đã chuyển thành công số banana là **{int(money):,d}** :banana: !"
            money_in_txt_2.write(str(money_left_after))
            money_give_in_txt_2.write(str(money_given))
        return answers
    def kiem_tra(tag):
        money_in_txt = open(f'assets\\information_id\\{tag}.txt')
        money= money_in_txt.read()
        answers = f"số banana của bạn hiện tại là **{int(money):,d}** :banana: !"
        return answers