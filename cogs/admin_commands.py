import disnake
from disnake.ext import commands

Duration = commands.option_enum({
    "30 секунд": 30,
    "3 минут": 180,
    "5 минут": 300,
    "10 минут": 600,
    "25 минут": 1500,
})


class UserCommands(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        
    
    @commands.slash_command(name="kick-member", description="Команда для кика пользователей")
    @commands.has_permissions(administrator=True, kick_members=True)
    async def kick_member(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, *args) -> None:
        """ 
        Parameters
        ----------
        member: Тег пользователя
        """
        await inter.response.send_message(f"**{inter.author.global_name}** выгнал участника **{member.global_name}**.")
        await member.kick()
        
    @commands.slash_command(name="time-out", description="команда для мута челиков")
    @commands.has_permissions(administrator=True)
    async def time_out(self, inter: disnake.ApplicationCommandInteraction,
                       member: disnake.Member, duration: Duration) -> None:
        """  
        Parameters
        ----------
        member: Выберите участника для мута
        duration: Как долго будет в муте
        """
        await member.timeout(duration=duration)
        await inter.response.send_message(f"Пользователь {member.global_name} отправляется в мут")
        

def setup(client) -> None:
    client.add_cog(UserCommands(client))