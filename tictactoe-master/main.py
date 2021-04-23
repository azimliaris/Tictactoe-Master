import state
import player
import humanplayer

if __name__ == "__main__":
    # training
    p1 = player.Player("p1")
    p2 = player.Player("p2")

    st = state.State(p1, p2)
    print("training...")
    st.play(50000)
    p1.savePolicy()

    # play with human
    print("Seeing results of trained agent")
    p1 = player.Player("computer", exp_rate=0)
    p1.loadPolicy("policy_p1")
    p2.exp_rate=0

    st = state.State(p1, p2)
    st.play(5000)


    p3 = humanplayer.HumanPlayer("human")

    st = state.State(p1, p3)
    st.play2()