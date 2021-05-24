from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(el) for el in input().split()]
locks = [int(el) for el in input().split()]
intelligence_value = int(input())
bullet_cost = 0
shooted = deque([])
locked = deque(locks)
locks_index = 0
counter = 0
for index in range(0, len(bullets)):
    shooted.append(bullets.pop())
    if int(shooted[index]) <= int(locked[locks_index]):
        locked.popleft()
        print("Bang!")
        counter += 1
        if not locked:
            if counter == gun_barrel_size:
                if bullets:
                    print("Reloading!")
                counter = 0
            print(f"{len(bullets)} bullets left. Earned ${abs(len(shooted * bullet_price) - intelligence_value)}")
            exit()
    else:
        print("Ping!")
        counter += 1
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locked)}")
        exit()

    else:
        if counter == gun_barrel_size:
            print("Reloading!")
            counter = 0

# int priceOfBullet = int.Parse(Console.ReadLine());
#             int gunBarrelSize = int.Parse(Console.ReadLine()); // count bullet in barrel
#             var bullets = new Stack<int>(Console.ReadLine().Split().Select(int.Parse).ToArray());
#             var locks = new Queue<int>(Console.ReadLine().Split().Select(int.Parse).ToArray());
#             var intelligence = int.Parse(Console.ReadLine());
#
#             int countBullet = bullets.Count;
#             int counterBullet = 0;
#             ;
#             while (true)
#             {
#                 if(bullets.Count == 0 || locks.Count == 0)
#                     break;
#
#                 var bullet = bullets.Peek();
#                 var lok = locks.Peek();
#
#                 if (bullet <= lok)
#                 {
#                     Console.WriteLine("Bang!");
#                     locks.Dequeue();
#                 }
#                 else
#                 {
#                     Console.WriteLine("Ping!");
#                 }
#
#                 bullets.Pop();
#                 counterBullet++;
#                 if (counterBullet == gunBarrelSize && bullets.Count != 0)
#                 {
#                     counterBullet = 0;
#                     Console.WriteLine("Reloading!");
#                 }
#             }
#
#             countBullet -= bullets.Count;
#             var bulletsCost = countBullet * priceOfBullet;
#
#             if (locks.Count == 0)
#             {
#                 Console.WriteLine($"{bullets.Count} bullets left. Earned ${intelligence - bulletsCost}");
#             }
#             else
#             {
#                 Console.WriteLine($"Couldn't get through. Locks left: {locks.Count}");
#             }
