# VARK Learning Style Questionnaire
# Author: Dahan TIMINAI (202412232)
# Description: Interactive Python program to determine a user's VARK learning style.

class InvalidChoiceException(Exception):
    """Exception raised for an invalid answer choice (not a/b/c/d)."""
    pass

class DuplicateAnswerException(Exception):
    """Exception raised for selecting an already chosen answer."""
    pass

class VARK:
    """Class to conduct the VARK learning style questionnaire."""

    # Class-level dictionary for learning styles
    LEARNING_STYLES = {
        "V": "Visual",
        "A": "Auditory",
        "R": "Read/Write",
        "K": "Kinaesthetic"
    }

    def __init__(self):
        """
        Initialize the VARK questionnaire with questions and scores.
        """

        # Questions and options stored as a list of dictionaries
        self.questions = [
            {"q": "1. You are helping someone who wants to go to your airport, town centre or railway station. You would:",
             "options": {"a": "go with her.", "b": "tell her the directions.", "c": "write down the directions.", "d": "draw, or give her a map."},
             "scores": {"a": "K", "b": "A", "c": "R", "d": "V"}},

            {"q": "2. You are not sure whether a word should be spelled 'dependent' or 'dependant'. You would:",
             "options": {"a": "see the words in your mind and choose by the way they look.", "b": "think about how each word sounds and choose one.", "c": "find it in a dictionary.", "d": "write both words on paper and choose one."},
             "scores": {"a": "V", "b": "A", "c": "R", "d": "K"}},

             {"q": "3. You are planning a holiday for a group. You want some feedback from them about the plan. You would:",
             "options": {"a": "describe some of the highlights.", "b": "use a map or website to show them the places.", "c": "give them a copy of the printed itinerary.", "d": "phone, text or email them."},
             "scores": {"a": "K", "b": "V", "c": "R", "d": "A"}},

            {"q": "4. You are going to cook something as a special treat for your family. You would:",
             "options": {"a": "cook something you know without the need for instructions.", "b": "ask friends for suggestions.", "c": "look through the cookbook for ideas from the pictures.", "d": "use a cookbook where you know there is a good recipe."},
             "scores": {"a": "K", "b": "A", "c": "V", "d": "R"}},

            {"q": "5. A group of tourists want to learn about the parks or nature reserves in your area. You would:",
             "options": {"a": "talk about, or arrange a talk.", "b": "show them internet pictures or books.", "c": "take them and walk with them.", "d": "give them a book or pamphlets."},
             "scores": {"a": "A", "b": "V", "c": "K", "d": "R"}},

            {"q": "6. You are about to purchase a digital camera or mobile phone. Other than price, what would most influence your decision?",
             "options": {"a": "Trying or testing it.", "b": "Reading the details about its features.", "c": "It is a modern design and looks good.", "d": "The salesperson telling you about its features."},
             "scores": {"a": "K", "b": "R", "c": "V", "d": "A"}},

            {"q": "7. Remember a time when you learned how to do something new. You learned best by:",
             "options": {"a": "watching a demonstration.", "b": "listening to somebody explaining it.", "c": "diagrams and charts.", "d": "written instructions."},
             "scores": {"a": "K", "b": "A", "c": "V", "d": "R"}},

            {"q": "8. You have a problem with your knee. You would prefer the doctor:",
             "options": {"a": "gave you something to read.", "b": "used a model of a knee.", "c": "described what was wrong.", "d": "showed you a diagram."},
             "scores": {"a": "R", "b": "K", "c": "A", "d": "V"}},

            {"q": "9. You want to learn a new program or game. You would:",
             "options": {"a": "read the manual.", "b": "talk to someone who knows it.", "c": "use the controls or keyboard.", "d": "follow diagrams in the book."},
             "scores": {"a": "R", "b": "A", "c": "K", "d": "V"}},

            {"q": "10. I like websites that have:",
             "options": {"a": "things I can click or try.", "b": "interesting visual design.", "c": "detailed written info.", "d": "audio like music or interviews."},
             "scores": {"a": "K", "b": "V", "c": "R", "d": "A"}},

            {"q": "11. What would most influence your decision to buy a non-fiction book?",
             "options": {"a": "The way it looks.", "b": "Reading parts of it.", "c": "A friend recommends it.", "d": "It has real-life examples."},
             "scores": {"a": "V", "b": "R", "c": "A", "d": "K"}},

            {"q": "12. You're learning how to use your new camera. You would prefer:",
             "options": {"a": "to ask questions and talk.", "b": "written instructions.", "c": "diagrams of parts.", "d": "examples of good and bad photos."},
             "scores": {"a": "A", "b": "R", "c": "V", "d": "K"}},

            {"q": "13. Do you prefer a presenter who uses:",
             "options": {"a": "practical sessions.", "b": "discussion or Q&A.", "c": "handouts or books.", "d": "graphs and charts."},
             "scores": {"a": "K", "b": "A", "c": "R", "d": "V"}},

            {"q": "14. You finished a test and want feedback. You would prefer:",
             "options": {"a": "examples of what you did.", "b": "written feedback.", "c": "talk it through.", "d": "graphs of performance."},
             "scores": {"a": "K", "b": "R", "c": "A", "d": "V"}},

            {"q": "15. Choosing food at a restaurant, you would:",
             "options": {"a": "choose what you've had before.", "b": "ask friends or waiter.", "c": "read the menu.", "d": "look at others' food or pictures."},
             "scores": {"a": "K", "b": "A", "c": "R", "d": "V"}},
             
            {"q": "16. Making an important speech, you would:",
             "options": {"a": "use diagrams/graphs.", "b": "write keywords and rehearse.", "c": "write out and read the full speech.", "d": "use examples and stories."},
             "scores": {"a": "V", "b": "A", "c": "R", "d": "K"}}
        ]

        # Initialize scores
        self.scores = {key: 0 for key in self.LEARNING_STYLES.keys()}

    def score_answer(self, answer, scores):
        """
        Update the score based on the user's answer.

        Args:
            answer (str): The user's answer key (e.g., 'a', 'b', 'c', 'd').
            scores (dict): Mapping of answer keys to learning style codes.
        """

        self.scores[scores[answer]] += 1

    def display_results(self):
        """
        Display the user's VARK results and provide insights based on their preferences.
        """

        print("\nYour VARK Results:")
        for key, value in self.scores.items():
            print(f"{self.LEARNING_STYLES[key]}: {value}")

        highest_score = max(self.scores.values())
        preferences = [k for k, v in self.scores.items() if v == highest_score]

        print("\nYour preferred learning style(s):")
        for pref in preferences:
            print(f"- {self.LEARNING_STYLES[pref]}")
        print()

        # Map sets of preferences to messages
        insights = {
            frozenset(["V"]): "You are a visual learner. You learn best through diagrams, charts, maps, and symbols. You prefer seeing information to understand it clearly.",
            frozenset(["A"]): "You are an auditory learner. You grasp information best by listening. Discussions, lectures, and talking things through help you understand concepts.",
            frozenset(["R"]): "You are a read/write learner. You prefer to learn through written words. You excel at reading texts and taking notes to absorb information.",
            frozenset(["K"]): "You are a kinaesthetic learner. You learn best by doing. Hands-on activities, experiments, and real-life examples help you retain knowledge.",
            frozenset(["V", "A"]): "You learn well through both visuals and listening. Diagrams and spoken explanations work together to enhance your understanding.",
            frozenset(["V", "R"]): "You prefer visual materials and written text. Charts, diagrams, and notes help you engage more deeply with information.",
            frozenset(["V", "K"]): "You thrive on both visual inputs and hands-on experiences. Seeing and doing help you grasp and apply new concepts.",
            frozenset(["A", "R"]): "You understand best through listening and reading. Combining spoken explanations with text-based resources helps reinforce your learning.",
            frozenset(["A", "K"]): "You learn by hearing and doing. Lectures, discussions, and practical experiences support your learning style well.",
            frozenset(["R", "K"]): "You benefit from both writing and doing. Taking notes and engaging in hands-on activities helps you process and retain information.",
            frozenset(["V", "A", "R"]): "You learn best when you can see, hear, and read. A combination of visuals, lectures, and written materials makes learning more effective for you",
            frozenset(["V", "A", "K"]): "You benefit from a mix of visual aids, spoken explanations, and physical activities. Seeing, hearing, and doing help you fully understand.",
            frozenset(["V", "R", "K"]): "You combine visual, reading, and kinaesthetic strengths. Diagrams, notes, and hands-on tasks work best for your learning process.",
            frozenset(["A", "R", "K"]): "You absorb information best by hearing it, reading it, and applying it practically. You thrive when learning is active and varied.",
            frozenset(self.LEARNING_STYLES.keys()): "You are a flexible learner who uses all four learning styles. You adapt easily to different teaching methods and learn best when material is presented in multiple formats — visual, auditory, written, and practical."
        }

        print("Insight:")
        msg = insights.get(frozenset(preferences))
        print(msg)   

    def get_valid_answer(self, prompt, options, exclude=None):
        """
        Prompt the user for a valid answer, optionally excluding one option.

        Args:
            prompt (str): The prompt to display to the user.
            options (dict): The valid answer options.
            exclude (str, optional): An answer to exclude (e.g., already chosen).

        Returns:
            str: The user's valid answer, or 'q' to quit.
        """

        while True:
            try:
                print()
                ans = input(prompt).strip().lower()
                if ans == 'q':
                    print("Questionnaire exited. Thank you for participating!")
                    return 'q'
                if ans not in options:
                    raise InvalidChoiceException("Invalid choice. Please enter A, B, C, or D.")
                if exclude is not None and ans == exclude:
                    raise DuplicateAnswerException("Already selected. Please enter a different option.")
                return ans
            except InvalidChoiceException as e:
                print(e)
            except DuplicateAnswerException as e:
                print(e)
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt ignored. Please answer the question.")


    def start(self):
        """
        Run the VARK questionnaire, collect answers, and display the results.
        """

        print("Welcome to the VARK Questionnaire!\nFind Your Path, Learn Your Way.\n\nRead each question carefully and choose the answer which best explains your preference.\nYou can enter 'Q' to quit at any time.\n")
        for q in self.questions:
            print(q["q"])
            for key, value in q["options"].items():
                print(f"  {key.upper()}. {value}")

            # First answer
            ans = self.get_valid_answer("Enter your answer (A/B/C/D): ", q["options"])
            if ans == 'q':
                return
            self.score_answer(ans, q["scores"])

            # Ask for second option
            while True:
                second = input("Do you have a second option? (Y/N): ").strip().lower()
                if second in ('y', 'yes'):
                    ans2 = self.get_valid_answer("Enter your second answer (A/B/C/D): ", q["options"], exclude=ans)
                    if ans2 == 'q':
                        return
                    self.score_answer(ans2, q["scores"])
                    break
                elif second in ('n', 'no'):
                    break
                else:
                    print("Please answer 'yes' or 'no'.")

            print()

        self.display_results()

# Create an instance of the VARK class and run the program
if __name__ == "__main__":
    vark_program = VARK()
    vark_program.start()