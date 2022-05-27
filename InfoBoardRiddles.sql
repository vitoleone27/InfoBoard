-- MySQL dump 10.13  Distrib 8.0.20, for macos10.15 (x86_64)
--
-- Host: localhost    Database: SecondTest3
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Riddles`
--

DROP TABLE IF EXISTS `Riddles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Riddles` (
  `riddle` varchar(180) DEFAULT NULL,
  `answer` varchar(50) NOT NULL,
  PRIMARY KEY (`answer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Riddles`
--

LOCK TABLES `Riddles` WRITE;
/*!40000 ALTER TABLE `Riddles` DISABLE KEYS */;
INSERT INTO `Riddles` VALUES ('﻿\"With thieves I consort',' With the Vilest'),('What building has the most stories?','A library.'),('What goes in the water black and comes out red?','A lobster.'),('What has a single eye but cannot see?','A needle'),('What loses its head in the morning and gets it back at night?','A pillow'),('What is brown and sticky?','A stick.'),('Kings and queens may cling to power. And the jester\'s got his call. But, as you may all discover. The common one outranks them all.','Ace'),('Almost everyone needs it, asks for it, gives it. But almost nobody takes it.','Advice'),('What goes up but never comes down?','Age'),('I cost no money to use, or conscious effort to take part of. And as far as you can see, there is nothing to me. But without me, you are dead.','Air'),('Today he is there to trip you up. And he will torture you tomorrow. Yet he is also there to ease the pain, when you are lost in grief and sorrow.','Alcohol'),('What asks but never answers?','An owl'),('What do you throw out to use and take in when you\'re done?','Anchor'),('I\'m very tempting, so its said, I have a shiny coat of red, and my flesh is white beneath. I smell so sweet, taste good to eat, and help to guard your teeth.','Apple'),('I fly through the air on small feathered wings, seeking out life and destroying all things.','Arrow'),('Large as a mountain, small as a pea, endlessly swimming in a waterless sea.','Asteroid'),('When I\'m metal or wood, I help you get home. When I\'m flesh and I\'m blood. In the darkness I roam.','Bat'),('I am the yellow hem of the sea\'s blue skirt.','Beach'),('What is it that has four legs, one head, and a foot?','Bed'),('A warrior amongst the flowers, he bears a thrusting sword. He uses it whenever he must, to defend his golden hoard.','Bee'),('Thousands lay up gold within this house. But no man made it. Spears past counting guard this house, but no man wards it.','Beehive'),('You heart it speak, for it has a hard tongue. But it cannot breathe, for it has not a lung.','Bell'),('I am a fire\'s best friend. When fat, my body fills with wind. When pushed to thin, through my nose I blow. Then you can watch the embers glow.','Bellows'),('I am seen in the water. If seen in the sky, I am in the rainbow, a jay\'s feather, and lapis lazuli.','Blue'),('Weight in my belly, trees on my back, nails in my ribs, feet I do lack.','Boat'),('My life is often a volume of grief, your help is needed to turn a new leaf. Stiff is my spine and my body is pale. But I\'m always ready to tell a tale.','Book'),('Turns us on our backs, and open up our stomachs. You will be the wisest of men though at start a lummox.','Books'),('Two brothers we are, great burdens we bear. All day we are bitterly pressed. Yet this I will say, we are full all the day, and empty when go to rest.','Boots'),('I have a neck but no head. I have a body but no arm. I have a bottom but no leg.','Bottle'),('I am free for the taking. Through all of your life, though given but once at birth. I am less than nothing in weight, but will fell the strongest of you if held.','Breath'),('I\'m light as a feather, yet the strongest man can\'t hold me for more than 5 minutes. What am I?','Breath.'),('To cross the water I\'m the way, for water I\'m above. I touch it not and, truth to say, I neither swim nor move.','Bridge'),('I have a hundred legs, but cannot stand. I have a long neck, but no head. I cannot see. I\'m neat and tidy as can be.','Broom'),('What lies in a tunnel of darkness. That can only attack when pulled back?','Bullet'),('Flat as a leaf, round as a ring. Has two eyes, can\'t see a thing.','Button'),('No matter how little or how much you use me, you change me every month.','Calendar'),('I have one eye. See near and far. I hold the moments you treasure and the things that make you weep.','Camera'),('My life can be measured in hours. I serve by being devoured. Thin, I am quick. Fat, I am slow. Wind is my foe.','Candle'),('What kind of pet always stays on the floor?','Carpet'),('Halo of water, tongue of wood. Skin of stone, long I\'ve stood. My fingers short reach to the sky. Inside my heart men live and die.','Castle'),('Though desert men once called me God, today men call me mad. For I wag my tail when I am angry. And growl when I am glad.','Cat'),('I\'m not really more than holes tied to more holes. I\'m strong as good steel, though not as stiff as a pole.','Chain'),('I have legs but walk not, a strong back but work not. Two good arms but reach not. A seat but sit and tarry not.','Chair'),('What\'s black when you get it, red when you use it, and white when you\'re all through with it?','Charcoal'),('Not born, but from a Mother\'s body drawn. I hang until half of me is gone. I sleep in a cave until I grow old. Then valued for my hardened gold.','Cheese'),('I wear a red robe, with staff in hand, and a stone in my throat.','Cherry'),('A slow, solemn square-dance of warriors feinting. One by one they fall, warriors fainting, thirty-two on sixty-four.','Chess'),('What is it that given one, you\'ll have either two or none?','Choice'),('This thing runs but cannot walk, sometimes sings but never talks. Lacks arms, has hands; lacks a head but has a face.','Clock'),('I fly, yet I have no wings. I cry, yet I have no eyes. Darkness follows me. Lower light I never see.','Cloud'),('Black we are and much admired. Men seek us if they are tired. We tire the horse, comfort man. Guess this riddle if you can.','Coal'),('A little pool with two layers of wall around it. One white and soft and the other dark and hard. Amidst a light brown grassy lawn with an outline of a green grass.','Coconut'),('The man who made it didn\'t need it. The man who bought it didn\'t use it. The man who used it didn\'t want it.','Coffin'),('What can you catch but not throw?','Cold'),('Metal or bone I may be, many teeth I have and always bared. Yet my bite harms no one. And ladies delight in my touch.','Comb'),('I am so simple that I can only point. Yet I guide men all over the world.','Compass'),('Remove the outside. Cook the inside. Eat the outside. Throw away the inside.','Corn'),('The more of it there is, the less you see.','Darkness'),('Some try to hide, some try to cheat. But time will show, we always will meet. Try as you might, to guess my name. I promise you\'ll know, when you I do claim.','Death'),('What is put on a table, cut, but never eaten?','Deck'),('A tiny bead, like fragile glass, strung along a cord of grass.','Dew'),('What has six faces and twenty-one eyes?','Die'),('What wears a coat in the winter and pants in the summer?','Dog'),('I don\'t think or eat or slumber. Or move around or fear thunder. Just like you I look the same but I can\'t harm you or be your bane.','Doll'),('What kind of nut is empty at the center and has no shell.','Doughnut'),('A word I know, six letters it contains. Subtract just one and twelve remains.','Dozens'),('This is in a realm of true and in a realm false, but you experience me as you turn and toss.','Dream'),('Although my cow is dead, I still beat her What a racket she makes.','Drum'),('People are hired to get rid of me. I\'m often hiding under your bed. In time I\'ll always return you see. Bite me and you\'re surely dead.','Dust'),('The beginning of eternity, the end of time and space, the beginning of every end, the end of every place.','E'),('You heard me before, yet you hear me again, then I die. Until you call me again.','Echo'),('What has to be broken before it can be used?','Egg'),('Face with a tree, skin like the sea. A great beast I am. Yet vermin frightens me.','Elephant'),('What word starts with \'E\', ends with \'E\', but only has one letter? It is not the letter \'E\'.','Envelope'),('A hole in a pole, though I fill a hole in white. I\'m used more by the day, and less by the night.','Eye'),('Two horses, swiftest traveling, harnessed in a pair, and grazing ever in places. Distant from them.','Eyes'),('When set loose I fly away. Never so cursed as when I go astray.','Fart'),('It\'s in your hand though you can not feel it. Only you and time can reveal it.','Fate'),('I make you weak at the worst of all times. I keep you safe, I keep you fine. I make your hands sweat. And your heart grow cold. I visit the weak, but seldom the bold.','Fear'),('I am the outstretched fingers that seize and hold the wind. Wisdom flows from me in other hands. Upon me are sweet dreams dreamt, my merest touch brings laughter.','Feather'),('Long and think, red within, with a nail at the end.','Finger'),('I am always hungry, I must always be fed. The finger I lick will soon turn red.','Fire'),('Screaming, soaring seeking sky. Flowers of fire flying high. Eastern art from ancient time. Name me now and solve this rhyme.','Firework'),('Up on high I wave away but not a word can I say.','Flag'),('When they are caught, they are thrown away. When they escape, you itch all day.','Fleas'),('Who spends the day at the window, goes to the table for meals. And hides at night?','Fly'),('My second is performed by my first, and it is thought a thief by the marks of my whole might be caught.','Footstep'),('I bubble and laugh and spit water in your face. I am no lady, and I don\'t wear lace.','Fountain'),('I have four legs but no tail. Usually I am heard only at night.','Frog'),('Goes over all the hills and hollows. Bites hard, but never swallows.','Frost'),('In the middle of night, I surround the gong. In the middle of sight, I end the song.','G'),('Born of earth, but with none of its strength. Molded by flame, but with none of its power. Shaped','Glass'),('Without a bridle, or a saddle, across a thing I ride a-straddle. And those I ride, by help of me, though almost blind, are made to see.','Glasses'),('They have not flesh, nor feathers, nor scales, nor bone. Yet they have fingers and thumbs of their own.','Gloves'),('I drive men mad for love of me. Easily beaten, never free.','Gold'),('The sun bakes them, the hand breaks them, the foot treads on them, and the mouth tastes them.','Grapes'),('The sharp slim blade, that cuts the wind.','Grass'),('So cold, damp and dark this place. To stay you would refrain, yet those who occupy this place do never complain.','Grave'),('Long and slinky like a trout, never sings till it\'s guts come out.','Gun'),('What\'s in the middle of nowhere?','H'),('I have one, you have one. If you remove the first letter, a bit remains. If you remove the second, bit still remains. If you remove the third, it still remains.','Habit'),('Grows from the ground, bushes and grass, leaves of yellow, red and brow, unruly plants, get the axe, trim the hedge back down.','Hair'),('Two in a whole and four in a pair. And six in a trio you see. And eight\'s a quartet but what you must get. Is the name that fits just one of me?','Half'),('How far will a blind dog walk into a forest?','Halfway'),('They are many and one, they wave and they drum, Used to cover a state, they go with you everywhere.','Hands'),('Inside a burning house, this thing is best to make. And best to make it quickly, before the fire\'s too much to take.','Haste'),('If you break me, I do not stop working. If you touch me, I may be snared. If you lose me, nothing will matter.','Heart'),('What gets bigger the more you take away from it?','Hole'),('When you stop and look, you can always see me. If you try to touch, you cannot feel me. I cannot move, but as you near me, I will move away from you.','Horizon'),('What always goes to bed with his shoes on?','Horse'),('Power enough to smash ships and crush roofs. Yet it still must fear the sun.','Ice'),('Lighter than what I am made of, more of me is hidden than is seen. I am the bane of the mariner. A tooth within the sea.','Iceberg'),('Glittering points that downward thrust. Sparkling spears that never rust.','Icicles'),('What word has kst in the middle, in the beginning, and at the end?','Inkstand'),('What goes in the water red, and comes out black?','Iron'),('I can be cracked, I can be made. I can be told, I can be played.','Joke'),('What force and strength cannot get through. I, with a gentle touch, can do. Many in the street would stand. Were I not a friend at hand.','Key'),('What goes through a door but never goes in. And never comes out?','Keyhole'),('I love to dance and twist and prance. I shake my tail, as away I sail. Wingless I fly into the sky.','Kite'),('I have a title and many pages. I am a genteel of genteel descent. I am a killer veteran of war. I am a slave to my lord pledged to his service.','Knight'),('Iron roof, glass walls, burns and burns and never falls.','Lantern'),('I am the red tongue of the earth, that buries cities.','Lava'),('They\'re up near the sky, on something very tall. Sometimes they die, only then do they fall.','Leaves'),('I\'m sometimes white and always wrong. I can break a heart and hurt the strong. I can build love or tear it down. I can make a smile or bring a frown.','Lie'),('What an fill a room but takes up no space?','Light'),('A dagger thrust at my own heart, dictates the way I\'m swayed. Left I stand, and right I yield, to the twisting of the blade.','Lock'),('In your fire you hear me scream, creaking and whining, yet I am dead before you lay me in your hearth.','Log'),('What can touch someone once and last them a life time?','Love'),('What two things can you never eat for breakfast?','Lunch and dinner.'),('It occurs once in every minute. Twice in every moment and yet never in one hundred thousand years.','M'),('What has four legs in the morning, two legs in the afternoon, and three legs in the evening?','Man'),('Where can you find roads without cars, forests without trees and cities without houses?','Map'),('Tool of thief, toy of queen. Always used to be unseen. Sign of joy, sign of sorrow. Giving all likeness borrowed.','Mask'),('Take one out and scratch my head, I am now black but once was red.','Match'),('What can bring back the dead. Make us cry, make us laugh, make us young. Born in an instant yet lasts a life time?','Memory'),('I\'m a god. I\'m a planet. I measure heat.','Mercury'),('You can spin, wheel and twist. But this thing can turn without moving.','Milk'),('Something wholly unreal, yet seems real to I. Think my friend, tell me where does it lie?','Mind'),('Look into my face and I\'m everybody. Scratch my back and I\'m nobody.','Mirror'),('A hill full, a hole full, yet you cannot catch a bowl full.','Mist'),('What goes further the slower it goes?','Money'),('Always old, sometimes new. Never sad, sometimes blue. Never empty, sometimes full. Never pushes, always pulls.','Moon'),('What has roots as nobody sees, is taller than trees. Up, up it goes, and yet never grows?','Mountain'),('What kind of room has no windows or doors?','Mushroom'),('At the sound of me, men may dream. Or stamp their feet. At the sound of me, women may laugh. Or sometimes weep.','Music'),('Who works when he plays and plays when he works?','Musician'),('What happens every second, minute, month, and century. But not every hour, week, year, or decade?','N'),('I hide but my head is outside.','Nail'),('What is it that was given to you, belongs only to you. And yet your friends use it more than you do?','Name'),('What is long and slim, works in light. Has but one eye, and an awful bite?','Needle'),('A house of wood in a hidden place. Built without nails or glue. High above the earthen ground. It holds pale gems of blue.','Nest'),('Hold the tail, while I fish for you.','Net'),('I can be written, I can be spoken, I can be exposed, I can be broken.','News'),('Sometimes I am loud. And viewed with distaste. Poke out my \'eye\', then I\'m on the front of your face.','Noise'),('What word is the same written forward, backward and upside down?','Noon'),('Gets rid of bad ones, short and tall. Tightens when used, one size fits all.','Noose'),('Two little holes in the side of a hill. Just as you come to the cherry-red mill.','Nose'),('It is greater than God and more evil than the devil. The poor have it, the rich need it, and if you eat it you\'ll die.','Nothing'),('A little house full of meat, no door to go in and eat.','Nut'),('There is one in every corner and two in every room.','O'),('What is the difference between a grandmother and a granary?','one is one\'s born-kin, the other is one\'s corn-bin'),('Take off my skin, I won\'t cry, but you will.','Onion'),('Gold in a leather bag, swinging on a tree, money after honey in its time. Ills of a scurvy crew cured by the sea, reason in its season but no rhyme.','Orange'),('My first is in ocean but never in sea. My second\'s in wasp but never in bee. My third is in glider and also in flight. My whole is a creature that comes out at night.','Owl'),('The eight of us move forth and back. To protect our king from the foes attack.','Pawns'),('A seed am I, three letters make my name. Take away two and I still sound the same.','Pea'),('The strangest creature you\'ll ever find has two eyes in front and a hundred behind.','Peacock'),('A house with two occupants, sometimes one, rarely three. Break the walls, eat the boarders, then throw away me.','Peanut'),('Lovely and round, I shine with pale light, grown in the darkness, a lady\'s delight.','Pearl'),('I am the tool, for inspiring many. Buy me in the store, for not much more than a penny. Don\'t overuse me, or my usefulness will go.','Pen'),('I usually wear a yellow coat. I usually have a dark head. I make marks wherever I go.','Pencil'),('I am a box that holds black and white keys without locks. Yet they can unlock your soul.','Piano'),('My first is twice in apple but not once in tart. My second is in liver but not in heart. My third is in giant and also in ghost. Whole I\'m best when I am toast.','Pig'),('What makes a loud noise when changing its jacket. Becomes larger but weighs less?','Popcorn'),('A skin have I, more eyes than one. I can be very nice when I am done.','Potato'),('What can be swallowed, But can also swallow you?','Pride'),('He has married many women but has never married.','Priest'),('I cannot be other than what I am, until the man who made me dies. Power and glory will fall to me finally. Only when he last closes his eyes.','Prince'),('Three little letters. A paradox to some. The worse that it is, the better it becomes.','Pun'),('Different lights do make me strange, thus into different sizes I will change.','Pupil'),('Two in a corner, one in a room, none in a house, but one in a shelter.','R'),('Only two backbones and thousands of ribs.','Railroad'),('What is the thing which, once poured out, cannot be gathered again?','Rain'),('I have split the one into five. I am the circle that few will spy. I am the path that breaks and gives. I am the bow no man may bend.','Rainbow'),('Break it and it is better, immediately set and harder to break again.','Record'),('What can be heard and caught but never seen?','Remark'),('To unravel me you need a simple key, no key that was made by locksmith\'s hand. But a key that only I will understand.','Riddle'),('It has no top or bottom, but it can hold flesh, bones, and blood all at the same time.','Ring'),('What always runs but never walks, often murmurs, never talks. Has a bed but never sleeps, has a mouth but never eats?','River'),('I run through hills. I veer around mountains. I leap over rivers. And crawl through the forests. Step out your door to find me.','Road'),('Snake coiled round and round. Snake deep below the ground. Snake that\'s never had a head. Snake that binds but not with dread.','Rope'),('What\'s large on Saturday and Sunday. Small on Tuesday, Wednesday, and Thursday, and disappears on Monday and Friday?','S'),('What can burn the eyes, sting the mouth, yet be consumed?','Salt'),('What measures out time. Until in time all is smashed to it?','Sand'),('I bind it and it walks. I loose it and it stops.','Sandal'),('My teeth are sharp, my back is straight, to cut things up it is my fate.','Saw'),('I open wide and tight I shut, Sharp am I and paper-cut fingers too, so do take care, I\'m good and bad, so best beware.','Scissors'),('If you have it, you want to share it. If you share it, you don\'t have it.','Secret'),('I crawl on the earth. And rise on a pillar.','Shadow'),('Of these things - I have two. One for me - and one for you. And when you ask about the price, I simply smile and nod twice.','Sharing'),('What has a neck and no head, two arms but no hands?','Shirt'),('Hard iron on horse. Cow\'s hide on man.','Shoe'),('In buckles or lace, they help set the pace. The farther you go, the thinner they grow.','Shoes'),('What five-letter word becomes shorter when you add two more letters?','Short'),('What is round as a dishpan, deep as a tub, and still the oceans couldn\'t fill it up?','Sieve'),('No sooner spoken than broken.','Silence'),('A beggar\'s brother went out to sea and drowned. But the man who drowned had no brother. Who was the beggar to the man who drowned?','Sister'),('Double my number, I\'m less than a score. Half of my number is less than four. Add one to my double when bakers are near. Days of the week are still greater, I fear.','Six'),('Twigs and spheres and poles and plates. Join and bind to reason make.','Skeleton'),('A house full, a yard full, a chimney full, no one can get a spoonful.','Smoke'),('Who is he that runs without a leg. And his house on his back?','Snail'),('Long slim and slender. Dark as homemade thunder. Keen eyes and peaked nose. Scares the Devil wherever it goes.','Snake'),('As beautiful as the setting sun, as delicate as the morning dew. An angel\'s dusting from the stars. That can turn the Earth into a frosted moon.','Snow'),('I come in winter. I cannot see, hear, or feel. I can\'t eat, But you can eat parts of me.','Snowman'),('You use it between your head and your toes, the more it works the thinner it grows.','Soap'),('I cannot be felt, seen or touched. Yet I can be found in everybody. My existence is always in debate. Yet I have my own style of music.','Soul'),('What surrounds the world, yet dwells within a thimble?','Space'),('I move without wings, Between silken string, I leave as you find, My substance behind.','Spider'),('I have holes on the top and bottom. I have holes on my left and on my right. And I have holes in the middle, Yet I still hold water.','Sponge'),('We travel much, yet prisoners are, and close confined to boot. Yet with any horse, we will keep the pace, and will always go on foot.','Spurs'),('A nut cracker up in a tree.','Squirrel'),('What goes around the world and stays in a corner?','Stamp'),('With pointed fangs it sits in wait. With piercing force it doles out fate, over bloodless victims proclaiming its might. Eternally joining in a single bite.','Stapler'),('We are all around, yet to us you are half blind. Sunlight makes us invisible, and difficult to find.','Stars'),('Inside a great blue castle lives a shy young maid. She blushes in the morning and comes not out at night.','Sun'),('A dragons tooth in a mortals hand, I kill, I maim, I divide the land.','Sword'),('He has one and a person has two. A citizen has three. And a human being has four. A personality has five. And an inhabitant of earth has six.','Syllable'),('I occur twice in eternity. And I\'m always within sight.','T'),('Late afternoons I often bathe. I\'ll soak in water piping hot. My essence goes through. My see through clothes. Used up am I - I\'ve gone to pot.','Teabag'),('What starts with a \'T\', ends with a \'T\', and has T in it?','Teapot'),('You must keep this thing. Its loss will affect your brothers. For once yours is lost, it will soon be lost by others.','Temper'),('What is often returned, but never borrowed/','Thanks'),('I occur once in a minute...','The letter \'m\''),('What can\'t you see, hear or feel, until its too late. What shadows love, and shopkeepers hate?','Thief'),('An open ended barrel, it is shaped like a hive. It is filled with the flesh, and the flesh is alive.','Thimble'),('He stands beside the road. In a purple cap at tattered green cloak. Those who touch him, curse him.','Thistle'),('I walked and walked and at last I got it. I didn\'t want it. So I stopped and looked for it. When I found it, I threw it away.','Thorn'),('Used left or right, I get to travel over cobblestone or gravel. Used up, I vie for sweet success, used down, I cause men great duress.','Thumb'),('Fatherless and motherless. Born without sin, roared when it came into the world. And never spoke again.','Thunder'),('In we go, out we go. All around and in a row. Always, always steady flow. When we\'ll stop, you\'ll never known. In we go, out we go.','Tides'),('There are two meanings to me. With one I may need to be broken, with the other I hold on. My favorite characteristic is my charming dimple.','Tie'),('Until I am measured. I am not known, yet how you miss me when I have flown.','Time'),('Forward I\'m heavy, but backwards I\'m not.','Ton'),('Often held but never touched. Always wet but never rusts. Often bits but seldom bit. To use it well you must have wit.','Tongue'),('What gets wetter the more it dries.','Towel'),('I am mother and father, but never birth or nurse. I\'m rarely still, but I never wander.','Tree'),('Who is it that rows quickly with four oars, but never comes out from under his own roof?','Turtle'),('What goes up when the rain comes down?','Umbrella'),('My voice is tender, my waist is slender and I\'m often invited to play. Yet wherever I go, I must take my bow or else I have nothing to say.','Violin'),('What instrument can make any sound and be heart, but not touched or seen?','Voice'),('My thunder comes before the lightning. My lightning comes before the clouds. My rain dries all the land it touches.','Volcano'),('We are five little objects of an everyday sort. You will find us all in a tennis court.','Vowels'),('I run around the city, but I never move.','Wall'),('As soft as silk, as white as milk, as bitter as gall, a thick green wall, and a green coat covers me all.','Walnut'),('What animal keeps the best time?','Watchdog'),('Three lives have I. Gentle enough to soothe the skin. Light enough to caress the sky. Hard enough to crack rocks.','Water'),('The moon is my father. The sea is my mother. I have a million brothers. I die when I reach land.','Wave'),('As round as an apple. As deep as a cup. All the king\'s horses can\'t pull it up.','Well'),('I go around in circles, but always straight ahead. Never complain, no matter where I am led.','Wheel'),('A leathery snake, with a stinging bite. I\'ll stay coiled up, unless I must fight.','Whip'),('What flies forever, Rests never?','Wind'),('I have four wings but cannot fly. I never laugh and never cry. On the same spot always found, toiling away with little sound.','Windmill'),('There is an ancient invention. Still used in some parts of the world today. That allows people to see through walls.','Window'),('When young, I am sweet in the sun. When middle-aged, I make you gay. When old, I am valued more than ever.','Wine'),('I am the heart that does not beat. If cut, I bleed without blood. I can fly, but have no wings. I can float, but have no fins. I can sing, but have no mouth.','Wood'),('What is it that you must give before you can keep it.','Word'),('What does no man want, yet no man want to lose?','Work'),('Soldiers line up spaced with pride. Two long rows lined side by side. One sole unit can decide, if the rows will unit or divide.','Zipper');
/*!40000 ALTER TABLE `Riddles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-27  1:23:52
