
Задание №1
```mermaid
classDiagram
    class SmartLight {
        +int brightness
        +str color
        -bool is_on
        +turn_on()
        +turn_off()
        +set_color(new_color)
    }
```

Задание №2
```mermaid
classDiagram
    class CreditCard {
        +str owner_name
        #float balance
        -str number
        -str cvc
        -str pin
        
        +pay(amount, pin)
        -check_pin(pin) bool
        +get_balance() float
        +get_masked_number() str
    }
```

Задание №3
```mermaid
classDiagram
    class Character {
        +String name
        +int health
        +int level
        +move(direction)
        +take_damage(amount)
        +get_status()
    }
    
    class Archer {
        +int arrows_count
        +shoot(target)
        +reload_arrows(count)
    }
    
    class Knight {
        +int armor
        +int sword_damage
        +attack_sword(target)
        +block()
    }
    
    Archer --|> Character
    Knight --|> Character
```

Задание №4
```mermaid
classDiagram
    class Song {
        +str title
        +float duration
        +str artist
        +str genre
        +display_info()
    }
    
    class Playlist {
        +str name
        +list songs
        +add_song(song)
        +remove_song(title)
        +get_duration()
        +play()
        +shuffle()
        +search_song(keyword)
    }
    
    Playlist "1" *-- "0..*" Song : contains
```

Задание №5
```mermaid
classDiagram
    class Order {
        +int id
        +str status
        +float total_price
        +list~Item~ items
        +DeliveryAgent delivery_agent
        +calculate_total()
        +update_status(new_status)
        +assign_agent(agent)
    }
    
    class Item {
        +str name
        +float price
        +int quantity
        +calculate_cost()
    }
    
    class DeliveryAgent {
        +str agent_id
        +float speed
        +str status
        +assign_order(order)
        +get_eta(distance)
    }
    
    class Courier {
        +str phone
        +call_customer()
        +get_signature()
    }
    
    class Drone {
        +float altitude
        +float battery_level
        +take_off()
        +land()
        +check_battery()
    }
    
    Order "1" *-- "1..*" Item : contains
    Order "1" o-- "1" DeliveryAgent : assigned to
    Courier --|> DeliveryAgent
    Drone --|> DeliveryAgent
```

Задание №6
```mermaid
classDiagram
    class User {
        +str user_id
        +str username
        +str email
        -str password_hash
        +datetime created_at
        +list~Post~ posts
        +list~Comment~ comments
        +create_post(content)
        +add_friend(user)
        +get_profile_info()
    }
    
    class Post {
        +str post_id
        +str content
        +datetime created_at
        +int likes_count
        +User author
        +list~Comment~ comments
        +add_comment(user, content)
        +like()
        +edit_content(new_content)
    }
    
    class Comment {
        +str comment_id
        +str content
        +datetime created_at
        +User author
        +Post post
        +edit_content(new_content)
        +delete()
    }
    
    User "1" *-- "*" Post : creates
    Post "1" *-- "*" Comment : has
    Comment "1" o-- "1" User : authored by
```

Обоснование:
1.Пост не может быть без автора. Если удалить пользователя, его посты тоже удаляются.  

2.Комментарий не может быть без поста. Если удалить пост, комментарии тоже удаляются.  
  
3.Пользователь может существовать без комментариев. Если удалить комментарий, пользователь остаётся.