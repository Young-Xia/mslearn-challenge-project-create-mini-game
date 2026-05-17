import random

def play_rock_paper_scissors():
    """
    Minigame de Pedra, Papel, Tesoura (Rock, Paper, Scissors)
    O jogador compete contra o computador em rodadas
    """
    print("🎮 Bem-vindo ao jogo de Pedra, Papel, Tesoura! 🎮")
    print("=" * 50)
    print("Regras:")
    print("- Pedra vence Tesoura")
    print("- Tesoura vence Papel")
    print("- Papel vence Pedra")
    print("=" * 50 + "\n")
    
    # Variáveis para rastrear pontuação
    player_wins = 0
    computer_wins = 0
    draws = 0
    total_rounds = 0
    
    # Opções válidas do jogo
    valid_options = ['rock', 'paper', 'scissors', 'pedra', 'papel', 'tesoura']
    
    # Mapeamento de opções em português para inglês
    option_map = {
        'pedra': 'rock',
        'papel': 'paper',
        'tesoura': 'scissors'
    }
    
    playing = True
    
    while playing:
        total_rounds += 1
        print(f"\n--- Rodada {total_rounds} ---")
        
        # Obter escolha do jogador
        player_choice = input("Escolha: rock, paper ou scissors (ou pedra, papel, tesoura): ").lower().strip()
        
        # Converter português para inglês se necessário
        if player_choice in option_map:
            player_choice = option_map[player_choice]
        
        # Validar entrada do jogador
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("❌ Opção inválida! Por favor, digite: rock, paper ou scissors")
            total_rounds -= 1  # Não contar como rodada válida
            continue
        
        # Computador escolhe aleatoriamente
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print(f"Você escolheu: {player_choice}")
        print(f"Computador escolheu: {computer_choice}")
        
        # Determinar vencedor da rodada
        if player_choice == computer_choice:
            print("🤝 Empate!")
            draws += 1
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("🎉 Você venceu essa rodada!")
            player_wins += 1
        else:
            print("😔 Computador venceu essa rodada.")
            computer_wins += 1
        
        # Perguntar se quer jogar novamente
        play_again = input("\nDeseja jogar novamente? (sim/não): ").lower().strip()
        if play_again not in ['sim', 's', 'yes', 'y']:
            playing = False
    
    # Exibir pontuação final
    print("\n" + "=" * 50)
    print("🏆 PONTUAÇÃO FINAL 🏆")
    print("=" * 50)
    print(f"Total de rodadas: {total_rounds}")
    print(f"Vitórias: {player_wins}")
    print(f"Derrotas: {computer_wins}")
    print(f"Empates: {draws}")
    print("=" * 50)
    
    if player_wins > computer_wins:
        print(f"🎊 Parabéns! Você venceu com {player_wins} vitórias!")
    elif computer_wins > player_wins:
        print(f"O computador venceu com {computer_wins} vitórias.")
    else:
        print("Você e o computador empataram!")
    
    print("\nObrigado por jogar! 👋\n")

if __name__ == "__main__":
    play_rock_paper_scissors()
