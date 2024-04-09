import random


# Q. 1~12월 총 3년, 36개월 회사를 운영하고, 의사 결정 단위는 1달..

'''
안녕하세요
현재 날짜: 2024년 1월
현재 상황: 재고 몇 개이고, 돈이 얼마 있음. (inv#, bal$)
생산량?? 휴먼cpu로 입력 받게
==>
-- rep
demand#, prod#, sals#, inv#
profit$, inv$, sales$, no_sales$
bal$
'''

Current_balance = 3000 # 초기 회사 통장 잔고
inventory = 100 # 초기 재고량


basic_cost = 3000 # 매월 나가는 기본비

sales_profit = 200 # 개당 판매 이익

inventory_cost = 50 # 개당 재고 손해

production_cost = 100 # 개당 생산비용

no_sales_loss = 20 # 못 팔 때 개당 기대비용


for year in range(2024, 2027):
    for month in range(1, 13):
        # 현재 시간 및 회사 재정 상황 설명
        print('사장님, 현재 날짜는', year, '년', month, '월입니다')
        print('재고는', inventory, '이고,', '현재 회사 통장 잔고는', Current_balance, '입니다.')

        # 이번 달 생산량 결정
        production = int(input('이번 달 생산량을 몇 개로 하실건가요? > '))
        production_total_cost = production * production_cost

        # 이번 달 수요량 랜덤으로 설정
        demand = random.randint(month*50, month*200)
        
        inventory = production + inventory

        # 수요량보다 재고가 많을 때
        if inventory >= demand:
            inventory -= demand
            sales_count = demand
            sales_total_profit = sales_profit * sales_count
            inventory_total_cost = inventory * inventory_cost
            no_sales_count = 0
            no_sales_cost = 0
            total_profit = sales_total_profit - inventory_total_cost - production_total_cost - no_sales_cost - basic_cost
            Current_balance = Current_balance + total_profit

        # 수요량보다 재고가 적을 때
        else:
            sales_count = inventory
            sales_total_profit = sales_profit * sales_count
            no_sales_count = demand - inventory
            inventory = 0
            inventory_total_cost = inventory * inventory_cost
            no_sales_cost = no_sales_count * no_sales_loss
            total_profit = sales_total_profit - inventory_total_cost - production_total_cost - no_sales_cost - basic_cost
            Current_balance = Current_balance + total_profit

        print('rep------------------------------------------')
        print('이번 달 생산량은', production, '이고, 이번 달 수요량은', demand, '입니다.')
        print('판매 후 남은 재고량은', inventory, '입니다.')
        print('판매 개수는', sales_count, '이고, 재고 부족으로 판매하지 못한 개수는', no_sales_count, '입니다.')
        print('판매로 번 이득은 ',sales_total_profit, '이고,  생산 비용은', production_total_cost,'이고,  다음 달 나갈 재고 비용은', inventory_total_cost, '이고, 미판매로 인한 손해는', no_sales_cost,'입니다.')
        print('이번 달 총 이득은', total_profit, '이므로, 이번 달 회사 통장 잔고는', Current_balance, '입니다.')
        print()
