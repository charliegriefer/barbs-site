import textwrap
from typing import Dict, List


class AboutService:

    def __init__(self):
        pass

    def team_members(self) -> List[Dict]:
        members = [
            {"name": "Barbara Mumaugh", "role": "Founder", "image": "barb.png"},
            {"name": "Scarlett Grauer", "role": "Director", "image": "scarlett.png"},
            {"name": "Gina Benner", "role": "CEO", "image": "gina.png"},
            {"name": "Estela Lucero", "role": "Rescue Manager", "image": "estela.png"},
            {
                "name": "David Gonzales",
                "role": "Operations & Maintenance Manager",
                "image": "david_gonzales.png",
            },
            {"name": "Cirilo"},
            {"name": "Miguel"},
            {"name": "Julio"},
            {"name": "Erick"},
            {"name": "Ismael"},
            {"name": "Oscar"},
            {"name": "Vanessa"},
            {"name": "Ivon"},
            {"name": "Natali"},
            {"name": "Luz"},
            {"name": "Hilda"},
            {"name": "Adela"},
            {"name": "Consuelo"},
            {"name": "Karla Daniela", "image": "karla_daniela.png"},
            {"name": "Monica"},
            {"name": "Arturo"},
            {"name": "Araceli"},
            {"name": "Mariel"},
            {"name": "Perla"},
            {"name": "José Manuel", "image": "jose_manuel.png"},
        ]

        return members

    def board_members(self) -> List[Dict]:
        board_members = [
            {
                "name": "Kathy Fredrickson Willits",
                "image": "kathy.png",
                "bio": textwrap.dedent(
                    """
                    <p>Meet <strong>Kathy Fredrickson Willits</strong>, the dedicated President of Barb's Dog Rescue.
                    Kathy's compassionate journey at the rescue began nine years ago, sparked by an immediate
                    connection with Barney, a big, fluffy dog rescued from dire circumstances.</p>
                    <p>Her mission to find him a home led to a deeper involvement, where she has since given tours,
                    arranged adoptions, and now utilizes her extensive network to lead the organization, addressing
                    inquiries and enhancing community support.</p>
                    <p>Beyond her impactful work at the rescue, Kathy is a successful businesswoman. Her
                    entrepreneurial journey has been marked by strategic leadership and innovation, culminating
                    in the recent sale of her thriving business.</p>
                    <p>Married to Gregg, a real estate professional, since 2012, Kathy has faced personal losses
                    with resilience, continuing to inspire through her work and dedication. Always active and
                    far too dynamic to consider retiring, Kathy embodies leadership and compassion in every
                    facet of her life.</p>
                """
                ).strip(),
            },
            {
                "name": "Gail Lacy",
                "image": "gail.png",
                "bio": textwrap.dedent(
                    """
                    <p>My name is <strong>Gail Lacy</strong>. I was born and raised in Glendale, AZ, and have always
                    been an advocate for dogs. I once rescued two dogs from an abusive situation and helped find
                    them new homes.</p>
                    <p>Over 35 years ago I taught school. Every year we read a beautiful dog story about a young
                    boy in the late 1800s who saved money to buy his first hunting dog. My class would bring in
                    change or earnings and we would visit a rescue to donate our collection.</p>
                    <p>When I met Barb many years ago she made such a huge impact on me that I knew I had to help
                    with her mission. I started transporting dogs for other rescues and organized several successful
                    fundraisers where we collected money, food, toys, and supplies. An auction I planned was
                    interrupted by COVID, but with help we eventually held an online event and pulled it off.</p>
                    <p>When Barb asked me to be on the board I was honored. I became very close to Barb when she
                    became ill and I would help with appointments and care. My home became her home away from home.</p>
                    <p>I am so pleased with what we have all done to keep Barb's legacy and dream alive. She had the
                    best staff and board around, and I will continue to do what I can to keep the rescue going strong.
                    </p>
                """
                ).strip(),
            },
            {
                "name": "Gina Benner",
                "image": "gina.png",
                "bio": textwrap.dedent(
                    """
                    <p>Meet <strong>Gina Benner</strong>, a Prescott native and long-time Rocky Point vacationer. Gina
                    has woven her love for education and real estate into the fabric of her life. Initially a high
                    school business teacher, she transitioned to real estate in Prescott 17 years ago and has become a
                    trusted realtor in the community.</p>
                    <p>A proud mom to two sons, Gina's lifelong passion has been rescuing dogs. Her dedication deepened
                    in 2014 when she met Barb and became a devoted supporter of the rescue, helping many dogs find
                    new homes—some becoming permanent members of her family.</p>
                    <p>Gina considers her work with the rescue her third and most fulfilling career. Embracing every
                    moment, she plans to continue her rescue efforts 'til she drops, finding deep joy and purpose in
                    giving dogs a better life.</p>
                """
                ).strip(),
            },
            {
                "name": "Jenny Radigan",
                "image": "jenny.png",
                "bio": textwrap.dedent(
                    """
                    <p>Meet <strong>Jenny Radigan</strong>, mom of nine, dog rescuer, and a dedicated teacher. Living in
                    Mexico with a big, bustling, bark-filled household, Jenny teaches compassion and care through her
                    work with Barb's Dog Rescue and other rescues in Penasco.</p>
                    <p>Supported by her long-suffering husband, Tom, and her children's unending support, Jenny's desire
                    is to always be at the heart of the action. Proving every day that multitasking is her superpower,
                    life for Jenny is a constant adventure filled with lessons, love, and laughter.</p>
                """
                ).strip(),
            },
        ]

        return board_members
