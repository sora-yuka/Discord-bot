import disnake
from disnake.ext import commands


class Events(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
    
    
    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member) -> None:
        """ Авто выдача роли и приветствие новеньких """
        role = disnake.utils.get(member.guild.roles, id=1162271810675540039)
        channel = self.client.get_channel(1162242469203820595)
        embed = disnake.Embed(
            title="Знакомтесь, новый участник",
            description=f"{member.mention} категорически приветствуем тебя на этом сервере.",
            color=0x98FB98,
        )
        embed.set_thumbnail(url=member.avatar)
        await channel.send(embed=embed)
        await member.add_roles(role)


def setup(client) -> None:
    client.add_cog(Events(client))