"""This is a template for a custom chain.

Edit this file to implement your chain logic.
"""

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.prompts import FewShotChatMessagePromptTemplate
from langchain.schema.runnable import Runnable
import asyncio

async def run_chat_model(chat_model, chat_prompt):
    async for msg in chat_model.astream(chat_prompt):
        print(msg, end="", flush=True)

def get_chain() -> Runnable:
    """
    Constructs and returns a chat chain that is ready to run.
    """
    chat_model = ChatOpenAI()

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    example_prompt = ChatPromptTemplate.from_messages([
        ("human", "{input}"), 
        ("ai", "{output}")
    ])
    few_shot_prompt = FewShotChatMessagePromptTemplate(example_prompt=example_prompt, examples=examples)
    human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")

    history = "{history}"

    if history.strip() != "":
        prev_topics_template = "Here is a list of the users previous topic history, they are separated by a comma: {history}"
        previous_topics_prompt = SystemMessagePromptTemplate.from_template(prev_topics_template)
        chat_prompt = ChatPromptTemplate.from_messages([
            previous_topics_prompt,
            few_shot_prompt,
            system_message_prompt,
            human_message_prompt
        ])
    else:
        chat_prompt = ChatPromptTemplate.from_messages([
            few_shot_prompt,
            system_message_prompt,
            human_message_prompt
        ])

    asyncio.run(run_chat_model(chat_model, chat_prompt))

    return chat_prompt | chat_model

examples = [
    {
        "input": "Software Development",
        "output": 
"""
### 1. —-Fundamentals of Computer Science—-

- <-->Programming Languages<-->: Learn the syntax, semantics, and paradigms of languages like <-->Python<-->, <-->Java<-->, <-->C++<-->, and <-->JavaScript<-->.
- <-->Data Structures<--> & <-->Algorithms<-->: Understand arrays, lists, trees, graphs, sorting algorithms, search algorithms, and complexity analysis.
- <-->Computer Architecture<--> & <-->Operating Systems<-->: Basic understanding of <-->how computers work<-->, including <-->processors<-->, memory management, and OS functions.

### 2. <-->Software Development Process<-->

- <-->Software Development Life Cycle (SDLC)<-->: Study the stages of software development, including requirements, design, implementation, testing, deployment, and maintenance.
- <-->Agile Methodologies<-->: Learn about Agile principles, <-->Scrum<-->, <-->Kanban<-->, and other iterative development methods.
- <-->Version Control Systems<-->: Master tools like <-->Git<--> for tracking changes in source code during software development.

### 3. —-Software Design—-

- <-->Object-Oriented Design<-->: Principles like <-->encapsulation<-->, <-->inheritance<-->, and <-->polymorphism<-->.
- <-->Design Patterns<-->: Study common solutions to recurring design problems (e.g., <-->Singleton<-->, <-->Observer<-->, <-->Factory<-->).
- <-->Architecture Patterns<-->: Understanding <-->MVC<-->, <-->Microservices<-->, <-->Monolith<-->, etc.

### 4. -—Testing and Quality Assurance-—

- <-->Manual Testing<-->: Techniques for executing software to identify bugs.
- <-->Automated Testing<-->: Tools and frameworks for <-->automating tests<--> (e.g., Selenium, JUnit).
- <-->Performance Testing<-->: Ensuring software performs well under expected workload.

### 5. <-->Database Management<-->

- <-->SQL & NoSQL Databases<-->: Learn database design, <-->normalization<-->, <-->querying<-->, and database management systems like <-->MySQL<-->, <-->PostgreSQL<-->, <-->MongoDB<-->.
- ORM Tools: Understand <-->Object-Relational Mapping<--> tools like Hibernate, Entity Framework.

### 6. Software Deployment & Operations

- <-->Containers and Virtualization<-->: Tools like <-->Docker<--> and <-->Kubernetes<-->
- <-->Continuous Integration<-->/<-->Continuous Deployment<--> (CI/CD): Automation of software deployment using Jenkins, Travis CI.
- <-->Cloud Computing<-->: Basics of AWS, Azure, Google Cloud.

### 7. Soft Skills and Management

- Problem-Solving Skills: Critical for debugging and developing logical solutions.
- <-->Project Management<-->: Basics of managing software projects, timelines, and stakeholders.
- Communication Skills: Essential for collaboration and effective team dynamics.

### 8. Current Trends and Advanced Topics

- <-->Artificial Intelligence<--> and <-->Machine Learning<-->
- <-->Blockchain Technology<-->
- <-->Cybersecurity Fundamentals<-->

### Learning Resources

- Online Courses: Platforms like Coursera, Udemy, and edX offer courses in various aspects of software engineering.
- Books: Classic texts like "Clean Code" by Robert C. Martin, "Design Patterns" by the Gang of Four, and "Introduction to Algorithms" by Cormen et al.
- Coding Practice: Websites like LeetCode, HackerRank for practicing coding problems.
- Open Source Contribution: Engage with real-world projects on GitHub.

### Practical Application

- Personal Projects: Apply what you've learned in building your own software projects.
- Internships and Work Experience: Real-world experience is invaluable.

Remember, Software Engineering is a field of constant learning and adaptation. The technologies and best practices evolve, so staying updated with the latest trends and advancements is crucial.
"""
    },
    {
        "input": "Management",
        "output":
"""
### 1. <-->Introduction to Management<-->

- <-->Definition and Functions of Management<-->: Understand the roles and responsibilities of managers, including planning, organizing, leading, and controlling.
- <-->Management Theories<-->: Explore different theories of management, such as <-->scientific management<-->, <-->human relations theory<-->, and <-->contingency theory<-->.

### 2. <-->Planning and Decision Making<-->

- <-->Strategic Planning<-->: Develop long-term goals and strategies for an organization.
- <-->Operational Planning<-->: Create short-term plans to achieve specific objectives.
- <-->Decision-Making Process<-->: Learn how to make effective decisions by gathering information, evaluating options, and choosing the best course of action.

### 3. <-->Organizational Structure<-->

- <-->Types of Organizational Structures<-->: Understand different structures like <-->functional<-->, <-->divisional<-->, <-->matrix<-->, and <-->virtual<-->.
- <-->Organizational Culture<-->: Explore the values, beliefs, and behaviors that shape an organization's work environment.
- <-->Organizational Change<-->: Study strategies for managing and leading change within an organization.

### 4. <-->Leadership and Motivation<-->

- <-->Leadership Styles<-->: Explore different leadership styles, such as <-->autocratic<-->, <-->democratic<-->, and <-->transformational<-->.
- <-->Motivation Theories<-->: Understand theories like <-->Maslow's hierarchy of needs<-->, <-->Herzberg's two-factor theory<-->, and <-->Expectancy theory<-->.
- <-->Effective Communication<-->: Learn how to communicate effectively with team members and stakeholders.

### 5. <-->Human Resource Management<-->

- <-->Recruitment and Selection<-->: Develop strategies for attracting and hiring the right employees.
- <-->Performance Management<-->: Set performance goals, provide feedback, and evaluate employee performance.
- <-->Employee Development<-->: Implement training and development programs to enhance employee skills and knowledge.

### 6. <-->Project Management<-->

- <-->Project Planning<-->: Define project scope, create a timeline, and allocate resources.
- <-->Project Execution<-->: Coordinate tasks, monitor progress, and manage risks.
- <-->Project Evaluation<-->: Assess project outcomes and identify areas for improvement.

### 7. <-->Strategic Management<-->

- <-->SWOT Analysis<-->: Analyze an organization's strengths, weaknesses, opportunities, and threats.
- <-->Competitive Advantage<-->: Identify strategies to gain a competitive edge in the market.
- <-->Corporate Social Responsibility<-->: Consider the impact of business decisions on society and the environment.

### 8. <-->Ethics in Management<-->

- <-->Business Ethics<-->: Understand ethical principles and their application in business decision-making.
- <-->Corporate Governance<-->: Study the systems and processes that ensure ethical behavior within an organization.
"""
    }
]

template="""
As an intelligent assistant, your primary function is to facilitate learning on any topic a user is interested in. To provide tailored and in-depth guidance, you will have access to the user's learning history, which includes topics they have previously explored. This background knowledge enables you to offer specific and relevant information related to their current learning objectives. For instance, if a user has progressed from a general interest in iOS development to learning about Xcode, and now seeks to understand debugging techniques, you can provide focused insights specifically related to debugging in Xcode and iOS development.

Your responsibilities include:

1. Review the User's Learning History: Analyze the list of topics the user has previously studied to understand their learning journey and current knowledge level.
2. Identify Key Sub-Topics: Based on the main topic and the user's learning history, determine all critical sub-topics that are essential for mastering the main subject.
3. Optimize Information Presentation: Structure your response using lists, headers, and clear paragraphs to make the information easily digestible and conducive to learning.
4. Highlight Noteworthy Information: It is VITAL to encircle particularly important pieces of information or sub-topics with '<-->' markers. These highlights should be relevant to the user's learning path and current topic of interest, emphasizing the most crucial aspects for deeper exploration or understanding.
5. Pause for Thoughtful Consideration: Before responding, take a moment to ensure that your information is comprehensive, directly relevant to the user's learning history, well-organized, and includes vital highlighted sections.
6. Deliver a Detailed Overview: Present the information, ensuring it is rich in valuable details and includes highlighted noteworthy topics.

It is NOT your responsibility to instruct the user to click on sub topics. You should assume that the user will explore the highlighted sub-topics on their own.

For example, if a user is currently interested in 'Dog Grooming', and has a background in general pet care, you might highlight '<-->Specific Breed Grooming Techniques<-->' as an important sub-topic. Remember, the highlighted text can include any significant piece of information, not just titles.
""" 