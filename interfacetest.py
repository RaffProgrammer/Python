import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import unicodedata


#Idiom
language = 'pt'

# No accents
def remove_accent(text):
    normalized_text = unicodedata.normalize('NFD', text)
    return ''.join(c for c in normalized_text if not unicodedata.combining(c))

#Change
def toggle_language():
    global language
    if language == 'pt':
        language = 'en'
        language_button.config(text="Trocar para Português")
    else:
        language = 'pt'
        language_button.config(text="Switch to English")
    update_texts()

# Update the texts depending of the idiom
def update_texts():
    if language == 'pt':
        game_label.config(text="Selecione o Jogo:")
        select_game_button.config(text="Selecionar Jogo")
        lane_label.config(text="Selecione a Rota:")
        select_lane_button.config(text="Selecionar Rota")
        champion_label.config(text="Selecione o Campeão:")
        select_champion_button.config(text="Selecionar Campeão")
        role_label.config(text="Selecione a Função:")
        select_role_button.config(text="Selecionar Função")
        agent_label.config(text="Selecione o Agente:")
        select_agent_button.config(text="Selecionar Agente")
    else:
        game_label.config(text="Select Game:")
        select_game_button.config(text="Select Game")
        lane_label.config(text="Select Lane:")
        select_lane_button.config(text="Select Lane")
        champion_label.config(text="Select Champion:")
        select_champion_button.config(text="Select Champion")
        role_label.config(text="Select Role:")
        select_role_button.config(text="Select Role")
        agent_label.config(text="Select Agent:")
        select_agent_button.config(text="Select Agent")

#image
def show_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.resize((200, 200), Image.ANTIALIAS)  # Redimensiona a imagem para 200x200 px
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Mantém uma referência para a imagem para evitar garbage collection
        image_label.pack()
    except Exception as e:
        if language == 'pt':
            messagebox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")
        else:
            messagebox.showerror("Error", f"Failed to load image: {e}")

#Lanes nad characters
def on_select_game():
    game = game_var.get().strip().lower()
    if game in ['lol', 'league of legends', 'liga das lendas']:
        show_lane_selection()
    elif game in ['valorant', 'vava', 'vavs']:
        show_role_selection()
    else:
        if language == 'pt':
            messagebox.showerror("Erro", "Este jogo não é reconhecido.")
        else:
            messagebox.showerror("Error", "This game is not recognized.")

def show_lane_selection():
    lane_label.pack()
    lane_dropdown.pack()
    select_lane_button.pack()

def on_select_lane():
    lane = lane_var.get().strip().lower()
    if lane == 'top':
        show_champion_selection(['darius', 'garen', 'sett', 'malphite', 'mordekaiser'], 'top')
    elif lane in ['jungle', 'jg']:
        show_champion_selection(['warwick', 'rengar', 'shaco', 'jax', 'volibear'], 'jungle')
    elif lane == 'mid':
        show_champion_selection(['katarina', 'veigar', 'yasuo', 'lux', 'heimerdinger'], 'mid')
    elif lane == 'adc':
        show_champion_selection(['vayne', 'caitlyn', 'jinx', 'zeri', 'ashe'], 'adc')
    elif lane in ['support', 'sup']:
        show_champion_selection(['seraphine', 'soraka', 'leona', 'blitzcrank', 'morgana'], 'support')
    else:
        if language == 'pt':
            messagebox.showerror("Erro", "Esta rota não é reconhecida.")
        else:
            messagebox.showerror("Error", "This lane is not recognized.")

def show_champion_selection(champions, lane):
    champion_label.pack()
    champion_dropdown['values'] = champions
    champion_dropdown.pack()
    select_champion_button.config(command=lambda: on_select_champion(lane))
    select_champion_button.pack()

def on_select_champion(lane):
    champion = champion_var.get().strip().lower()
   
    #Lanes
    
    #Top lane
    if lane == 'top' and champion in ['darius', 'garen', 'sett', 'malphite', 'mordekaiser']:
        if champion == 'darius':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Darius, o Mão de Noxus, é um poderoso campeão top laner com um machado enorme e habilidades fortes de execução.')
            else:
                messagebox.showinfo("Selection", 'Darius, the Hand of Noxus, is a powerful top laner with a massive axe and strong execution abilities.')
        if champion == 'garen':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Garen, o Poder de Demacia, é um top laner durável, conhecido por seus golpes giratórios e forte resistência.')
            else:
                messagebox.showinfo("Selection", 'Garen, the Might of Demacia, is a durable top laner known for his spinning strikes and strong tankiness.')
        if champion == 'sett':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Sett, o Chefe, é um lutador da rota superior com socos poderosos e controle de grupo, dominando os inimigos com sua força bruta e habilidades táticas.')
            else:
                messagebox.showinfo("Selection", 'Sett, the Boss, is a brawler top laner with powerful punches and crowd control, dominating enemies with his raw strength and tactical abilities.')
        if champion == 'malphite':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Malphite, um enorme golem de pedra que se destaca em suportar dano e destruir inimigos com suas habilidades sísmicas.')
            else:
                messagebox.showinfo("Selection", 'Malphite, a massive rock golem who excels in tanking damage and disrupting enemies with his seismic abilities.')
        if champion == 'mordekaiser':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Mordekaiser, um poderoso rolo compressor que domina as lutas com sua imensa força e capacidade de controlar o campo de batalha com sua magia negra.')
            else:
                messagebox.showinfo("Selection", 'Mordekaiser, a powerful juggernaut who dominates fights with his immense strength and ability to control the battlefield with his dark magic.')
                
                #Jungle lane
    if lane == 'jungle' and champion in ['warwick', 'rengar', 'shaco', 'jax', 'volibear']:
        if champion == 'warwick':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Warwick, um caçador feroz que persegue e devora inimigos, usando seus sentidos aguçados e habilidades poderosas para se sustentar na batalha.')
            else:
                messagebox.showinfo("Selection", 'Warwick, a ferocious hunter who tracks down and devours enemies, using his enhanced senses and powerful abilities to sustain himself in battle.')
        if champion == 'rengar':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Rengar, um predador implacável que se destaca em emboscadas e grandes explosões de dano, usando suas habilidades de rastreamento e ferocidade para caçar inimigos.')
            else:
                messagebox.showinfo("Selection", 'Rengar, a relentless predator who excels in ambushes and high burst damage, using his tracking skills and ferocity to hunt down enemies.')
        if champion == 'shaco':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Shaco, um assassino enganador que se destaca em trapaça e furtividade, usando seus clones e armadilhas para surpreender e eliminar inimigos.')
            else:
                messagebox.showinfo("Selection", 'Shaco, a deceptive assassin who excels in trickery and stealth, using his clones and traps to surprise and eliminate enemies.')
        if champion == 'jax':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Jax, um lutador formidável que se destaca em duelos com seu alto dano e capacidade de virar o jogo com seus golpes poderosos.')
            else:
                messagebox.showinfo("Selection", 'Jax, a formidable fighter who excels in dueling with his high damage and ability to turn fights with his powerful strikes.')
        if champion == 'volibear':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Volibear, um poderoso berserker com a força de uma tempestade, se destaca em batalhas de linha de frente e esmaga inimigos com seus ataques ferozes e habilidades baseadas em raios.')
            else:
                messagebox.showinfo("Selection", 'Volibear, a mighty berserker with the strength of a thunderstorm, excels in frontline battles and crushing foes with his ferocious attacks and lightning-based abilities.')
                
                #Mid lane
    if lane == 'mid' and champion in ['katarina', 'veigar', 'yasuo', 'lux', 'heimerdinger']:
        if champion == 'katarina':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Katarina, a Lâmina Sinistra, é uma mid-laner de alto dano que se destaca em ataques rápidos e letais e pode eliminar inimigos rapidamente com sua agilidade e habilidades com adagas.')
            else:
                messagebox.showinfo("Selection", 'Katarina, the Sinister Blade, is a high-damage mid-laner who excels in swift, lethal attacks and can quickly eliminate enemies with her agility and dagger skills.')
        if champion == 'veigar':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Veigar, um mestre da magia negra que fica mais forte a cada feitiço, liberando explosões devastadoras de poder.')
            else:
                messagebox.showinfo("Selection", 'Veigar, a master of dark magic who grows stronger with each spell, unleashing devastating bursts of power.')
        if champion == 'yasuo':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Yasuo, um espadachim ágil que usa o vento para atravessar inimigos e desviar de ataques.')
            else:
                messagebox.showinfo("Selection", 'Yasuo, a nimble swordsman who wields the wind to dash through enemies and deflect attacks.')
        if champion == 'lux':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Lux, uma maga radiante que usa uma poderosa magia de luz para causar dano e proteger seus aliados.')
            else:
                messagebox.showinfo("Selection", 'Lux, a radiant mage who wields powerful light magic to deal damage and shield her allies.')
        if champion == 'heimerdinger':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Heimerdinger, um inventor brilhante que se destaca no controle do campo de batalha com suas torres e dispositivos poderosos.')
            else:
                messagebox.showinfo("Selection", 'Heimerdinger, a brilliant inventor who excels at controlling the battlefield with his turrets and powerful gadgets.')
               
                #Adc lane
    if lane == 'adc' and champion in ['vayne', 'caitlyn', 'jinx', 'zeri', 'ashe']:
        if champion == 'vayne':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Vayne, um atirador mortal que se destaca em furtividade e agilidade, caçando inimigos com precisão e alto dano explosivo.')
            else:
                messagebox.showinfo("Selection", 'Vayne, a deadly marksman who excels in stealth and agility, hunting down enemies with precision and high burst damage.')
        if champion == 'caitlyn':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Caitlyn, uma atiradora de elite que se destaca em ataques de longo alcance, usando sua precisão e armadilhas para controlar o campo de batalha.')
            else:
                messagebox.showinfo("Selection", 'Caitlyn, a sharpshooter who excels at long-range attacks, using her precision and traps to control the battlefield.')
        if champion == 'jinx':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Jinx, uma criminosa caótica que se deleita com o caos, usando armas explosivas e tiros rápidos para desmantelar seus inimigos.')
            else:
                messagebox.showinfo("Selection", 'Jinx, a chaotic criminal who revels in mayhem, using explosive weapons and rapid fire to dismantle her foes.')
        if champion == 'zeri':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Zeri, uma atiradora extremamente rápida que libera rajadas elétricas e ataques rápidos para subjugar seus inimigos.')
            else:
                messagebox.showinfo("Selection", 'Zeri, a lightning-fast marksman who unleashes electric bursts and rapid attacks to overwhelm her foes.')
        if champion == 'ashe':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Ashe, uma atiradora precisa que usa suas flechas de gelo e habilidades táticas para desacelerar e derrubar inimigos à distância.')
            else:
                messagebox.showinfo("Selection", 'Ashe, a precise marksman who uses her frost arrows and tactical abilities to slow and take down enemies from a distance.')
                
                #Sup lane
    if lane == 'support' and champion in ['seraphine', 'soraka', 'leona', 'blitzcrank', 'morgana']:
        if champion == 'seraphine':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Seraphine, a Cantora dos Olhos Estrelados, é uma mid-laner e suporte que usa seus talentos musicais para curar aliados, causar dano mágico e controlar o campo de batalha com suas habilidades harmoniosas.')
            else:
                messagebox.showinfo("Selection", 'Seraphine, the Starry-Eyed Songstress, is a mid-laner and support who uses her musical talents to heal allies, deal magic damage, and control the battlefield with her harmonious abilities.')
        if champion == 'soraka':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Soraka, uma curandeira celestial que usa seus poderes divinos para curar e proteger seus aliados, trazendo esperança e restauração no campo de batalha.')
            else:
                messagebox.showinfo("Selection", 'Soraka, a celestial healer who uses her divine powers to heal and protect her allies, bringing hope and restoration on the battlefield.')
        if champion == 'leona':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Leona, uma guerreira radiante que se destaca na proteção de sua equipe com escudos fortes e poderosas habilidades baseadas na luz solar.')
            else:
                messagebox.showinfo("Selection", 'Leona, a radiant warrior who excels in protecting her team with strong shields and powerful sunlight-based abilities.')
        if champion == 'blittzcrank':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Blitzcrank, um robô enorme com um poderoso gancho e habilidades de arremesso, é excelente em iniciar lutas e atrapalhar inimigos.')
            else:
                messagebox.showinfo("Selection", 'Blitzcrank, a massive robot with a powerful hook and knock-up abilities, excels at initiating fights and disrupting enemies.')
        if champion == 'morgana':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Morgana, uma feiticeira negra que usa sua magia para prender e debilitar inimigos enquanto protege aliados do perigo.')
            else:
                messagebox.showinfo("Selection", 'Morgana, a dark sorceress who uses her magic to trap and debilitate foes while shielding allies from harm.')
        

#Roles and characters

def show_role_selection():
    role_label.pack()
    role_dropdown.pack()
    select_role_button.pack()

def on_select_role():
    role = role_var.get().strip().lower()
    if role in ['duelist', 'atacante']:
        show_agent_selection(['raze', 'reyna', 'jett', 'phoenix', 'yoru'], 'duelist')
    elif role in ['sentinel', 'sentinela', 'sent']:
        show_agent_selection(['sage', 'cypher', 'killjoy', 'chamber', 'deadlock'], 'sentinel')
    elif role in ['initiator', 'iniciador']:
        show_agent_selection(['sova', 'breach', 'gekko', 'skye', 'kay/o'], 'initiator')
    elif role in ['controller', 'controlador']:
        show_agent_selection(['brimstone', 'omen', 'astra', 'harbor', 'viper'], 'controller')
    else:
        if language == 'pt':
            messagebox.showerror("Erro", "Esta função não é reconhecida.")
        else:
            messagebox.showerror("Error", "This role is not recognized.")

def show_agent_selection(agents, role):
    agent_label.pack()
    agent_dropdown['values'] = agents
    agent_dropdown.pack()
    select_agent_button.config(command=lambda: on_select_agent(role))
    select_agent_button.pack()

def on_select_agent(role):
    agent = agent_var.get().strip().lower()
    
    #Roles
    
    #Duelist role
    if role == 'duelist' and agent in ['raze', 'reyna', 'jett', 'phoenix', 'yoru']:
        if agent == 'raze':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Raze é uma duelista conhecida por suas habilidades explosivas.')
            else:
                messagebox.showinfo("Selection", 'Raze is a duelist known for her explosive abilities.')
        if agent == 'reyna':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Reyna é uma duelista autossuficiente que adora garantir mortes para se curar ou se tornar invulnerável, o que a torna uma força formidável em combates mano a mano.")
            else:
                messagebox.showinfo("Selection", 'Reyna is a self-sufficient duelist who thrives on securing kills to heal herself or become invulnerable, making her a formidable force in one-on-one combat.')
        if agent == 'jett':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Jett é uma duelista ágil que se destaca em mobilidade e agilidade, usando suas habilidades para correr, pular alto e lançar lâminas de vento, o que a torna uma atacante dinâmica e esquiva.")
            else:
                messagebox.showinfo("Selection", 'Jett is a nimble duelist who excels in mobility and agility, using her abilities to dash, jump high, and throw wind blades, making her a dynamic and elusive attacker.')
        if agent == 'phoenix':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Phoenix é um duelista que controla o fogo para causar dano e se curar. Suas habilidades incluem flashbangs, uma parede de fogo auto-reanimadora e uma poderosa bola de fogo.")
            else:
                messagebox.showinfo("Selection", 'Phoenix is a duelist who controls fire to deal damage and heal himself. His abilities include flashbangs, a self-reviving fire wall, and a powerful fireball.')
        if agent == 'yoru':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Yoru é um duelista especializado em dissimulação e furtividade. Ele pode se teletransportar, criar chamarizes e usar uma poderosa granada de luz para desorientar inimigos e superar oponentes.")
            else:
                messagebox.showinfo("Selection", 'Yoru is a duelist who specializes in deception and stealth. He can teleport, create decoys, and use a powerful flashbang to disorient enemies and outmaneuver opponents.')

                #Sentinel role
    if role == 'sentinel' and agent in ['sage', 'cypher', 'killjoy', 'chamber', 'deadlock']:
        if agent == 'sage':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Sage é uma sentinela que se destaca em curar e proteger sua equipe. Ela pode curar aliados, criar barreiras para bloquear caminhos e ressuscitar companheiros de equipe caídos.')
            else:
                messagebox.showinfo("Selection", 'Sage is a sentinel who excels in healing and protecting her team. She can heal allies, create barriers to block paths, and resurrect fallen teammates.')
        if agent == 'cypher':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Cypher é um sentinela focado em coletar informações. Ele usa armadilhas, câmeras e fios de disparo para monitorar os movimentos inimigos e controlar o campo de batalha.")
            else:
                messagebox.showinfo("Selection", 'Cypher is a sentinel focused on gathering intel. He uses traps, cameras, and tripwires to monitor enemy movements and control the battlefield.')
        if agent == 'killjoy':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Killjoy é uma sentinela que usa dispositivos para controlar o campo de batalha. Suas habilidades incluem implantar uma torre, um bot de alarme e granadas nanoswarm para interromper e causar dano aos inimigos.")
            else:
                messagebox.showinfo("Selection", 'Killjoy is a sentinel who uses gadgets to control the battlefield. Her abilities include deploying a turret, alarm bot, and nanoswarm grenades to disrupt and damage enemies.')
        if agent == 'chamber':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Chamber é um sentinela com foco em precisão e controle. Ele usa suas armas personalizadas, âncoras de teletransporte e armadilhas para garantir mortes e manter áreas com precisão mortal.")
            else:
                messagebox.showinfo("Selection", 'Chamber is a sentinel with a focus on precision and control. He uses his custom weapons, teleportation anchors, and traps to secure kills and hold down areas with deadly accuracy.')
        if agent == 'deadLock':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Deadlock é uma sentinela que usa tecnologia avançada para controlar áreas. Ela implanta barreiras, armadilhas e um ultimate poderoso que imobiliza e captura inimigos, tornando-a uma força estratégica para interromper oponentes.")
            else:
                messagebox.showinfo("Selection", 'Deadlock is a sentinel who uses advanced technology to control areas. She deploys barriers, traps, and a powerful ultimate that immobilizes and captures enemies, making her a strategic force in disrupting opponents.')
                 
                 #Initiator role
    if role == 'Initiator' and agent in ['sova', 'breach', 'gekko', 'skye', 'kay/o']:
        if agent == 'sova':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Sova é um iniciador que se destaca em coletar informações. Ele usa seu raio de reconhecimento, drone e habilidade suprema para localizar e revelar inimigos, permitindo que sua equipe planeje e execute ataques de forma eficaz.')
            else:
                messagebox.showinfo("Selection", 'Sova is an initiator who excels in gathering information. He uses his recon bolt, drone, and ultimate ability to locate and reveal enemies, allowing his team to plan and execute attacks effectively.')
        if agent == 'breach':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Breach é um iniciador especializado em negação de área e controle de multidões. Ele usa explosões sísmicas e cargas concussivas para atordoar e desorientar inimigos, abrindo caminho para sua equipe avançar.")
            else:
                messagebox.showinfo("Selection", 'Breach is an initiator who specializes in area denial and crowd control. He uses seismic blasts and concussive charges to stun and disorient enemies, clearing paths for his team to advance.')
        if agent == 'gekko':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Gekko é um iniciador que usa suas criaturas para interromper inimigos e dar suporte ao seu time. Suas habilidades incluem enviar companheiros para atordoar, cegar ou deter oponentes, tornando-o versátil tanto no ataque quanto na defesa.")
            else:
                messagebox.showinfo("Selection", 'Gekko is an initiator who uses his creatures to disrupt enemies and support his team. His abilities include sending out companions to stun, blind, or detain opponents, making him versatile in both offense and defense.')
        if agent == 'skye':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Skye é uma iniciadora que apoia sua equipe com cura e reconhecimento. Ela usa seus companheiros animais para piscar, atordoar e revelar inimigos enquanto fornece cura para seus aliados.")
            else:
                messagebox.showinfo("Selection", 'Skye is an initiator who supports her team with healing and reconnaissance. She uses her animal companions to flash, stun, and reveal enemies while providing healing to her allies.')
        if agent == 'kay/o':
            if language == 'pt':
                messagebox.showinfo("Seleção", "KAY/O é um iniciador que se destaca em interrupção e suporte. Ele pode suprimir habilidades inimigas, lançar uma granada de fragmentação e usar seu ultimate para aumentar o dano de sua equipe e fornecer um estímulo de combate.")
            else:
                messagebox.showinfo("Selection", 'KAY/O is an initiator who excels in disruption and support. He can suppress enemy abilities, throw a frag grenade, and use his ultimate to enhance his team\'s damage and provide a combat stim.')
                
                #Controller role
    if role == 'controller' and agent in ['brimstone', 'omen', 'astra', 'harbor', 'viper']:
        if agent == 'brimstone':
            if language == 'pt':
                messagebox.showinfo("Seleção", 'Brimstone é um controlador que se destaca em suporte tático. Ele usa cortinas de fumaça para obscurecer a visão, granadas incendiárias para negar áreas e um ataque orbital para causar dano de área, dando à sua equipe uma vantagem estratégica.')
            else:
                messagebox.showinfo("Selection", 'Brimstone is a controller who excels in tactical support. He uses smoke screens to obscure vision, incendiary grenades to deny areas, and an orbital strike for area damage, giving his team a strategic edge.')
        if agent == 'omen':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Omen é um controlador especializado em furtividade e interrupção. Ele usa cortinas de fumaça para obscurecer a visão, uma habilidade de teletransporte para se reposicionar e um ultimate que revela a localização dos inimigos e os desorienta.")
            else:
                messagebox.showinfo("Selection", 'Omen is a controller who specializes in stealth and disruption. He uses smokescreens to obscure vision, a teleportation ability to reposition himself, and an ultimate that reveals enemies\' locations and disorients them.')
        if agent == 'astra':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Astra é uma controladora que manipula o espaço com suas habilidades cósmicas. Ela pode colocar estrelas no mapa para criar fumaças, flashes e puxões gravitacionais, e seu ultimate permite que ela reposicione e controle áreas de qualquer lugar do mapa.")
            else:
                messagebox.showinfo("Selection", 'Astra is a controller who manipulates space with her cosmic abilities. She can place stars on the map to create smokes, flashes, and gravitational pulls, and her ultimate allows her to reposition and control areas from anywhere on the map.')
        if agent == 'harbor':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Harbor é um controlador que usa habilidades baseadas em água para controlar o campo de batalha. Ele pode implantar barreiras de água para bloquear a visão, criar ondas que retardam os inimigos e usar uma poderosa onda de maré final para interromper e causar dano aos oponentes em uma área ampla.")
            else:
                messagebox.showinfo("Selection", 'Harbor is a controller who uses water-based abilities to control the battlefield. He can deploy water barriers to block vision, create waves that slow enemies, and use a powerful tidal wave ultimate to disrupt and damage opponents in a wide area.')
        if agent == 'viper':
            if language == 'pt':
                messagebox.showinfo("Seleção", "Viper é uma controladora que se destaca em negação de área e habilidades baseadas em veneno. Ela usa telas tóxicas para obscurecer a visão, implanta nuvens de veneno e poças de ácido para causar dano e debuff aos inimigos, e seu ultimate cria uma zona tóxica massiva que causa dano ao longo do tempo e fornece à sua equipe uma vantagem tática.")
            else:
                messagebox.showinfo("Selection", 'Viper is a controller who excels in area denial and poison-based abilities. She uses toxic screens to obscure vision, deploys poison clouds and acid pools to damage and debuff enemies, and her ultimate creates a massive toxic zone that deals damage over time and provides her team with a tactical advantage.')


# principal window
root = tk.Tk()
root.title("Seleção de Jogo")

# Variable to keep lanes, roles and etc
game_var = tk.StringVar()
lane_var = tk.StringVar()
champion_var = tk.StringVar()
role_var = tk.StringVar()
agent_var = tk.StringVar()

# Widgets de seleção de jogo
game_label = ttk.Label(root, text="Selecione o Jogo:")
game_label.pack()

game_dropdown = ttk.Combobox(root, textvariable=game_var, values=['LoL', 'Valorant'])
game_dropdown.pack()

select_game_button = ttk.Button(root, text="Selecionar Jogo", command=on_select_game)
select_game_button.pack()

# Widgets adicionais (inicialmente ocultos)
lane_label = ttk.Label(root, text="Selecione a Rota:")
lane_dropdown = ttk.Combobox(root, textvariable=lane_var)

select_lane_button = ttk.Button(root, text="Selecionar Rota", command=on_select_lane)

champion_label = ttk.Label(root, text="Selecione o Campeão:")
champion_dropdown = ttk.Combobox(root, textvariable=champion_var)

select_champion_button = ttk.Button(root, text="Selecionar Campeão")

role_label = ttk.Label(root, text="Selecione a Função:")
role_dropdown = ttk.Combobox(root, textvariable=role_var)

select_role_button = ttk.Button(root, text="Selecionar Função", command=on_select_role)

agent_label = ttk.Label(root, text="Selecione o Agente:")
agent_dropdown = ttk.Combobox(root, textvariable=agent_var)

select_agent_button = ttk.Button(root, text="Selecionar Agente")

# Change Idiom 
language_button = ttk.Button(root, text="Switch to English", command=toggle_language)
language_button.pack()

# Start principal window loop
root.mainloop()
