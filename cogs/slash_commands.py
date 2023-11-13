import disnake
from disnake.ext import commands


class SlashCommands(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        
    
    @commands.slash_command(name="send-source", description="Команда для удобной компоновки ссылок.")
    async def send_source(
        self, iter: disnake.ApplicationCommandInteraction, 
        link_title: str, url: str, description: str
    ) -> None:
        
        """ 
        Parameters
        ----------
        link_title: Название для эмбеда
        url: Ссылка на источник
        description: Краткое описание материала
        """
        
        embed = disnake.Embed(title = link_title, color = 0x5C5CFF, url = url, description = f"**{description}**")
        embed.set_author(name = iter.author.global_name, icon_url = iter.author.avatar)
        embed.set_footer(text = "Бот еще в стадии разработки и будет не раз видо-изменяться.", 
                         icon_url = "https://i.pinimg.com/564x/aa/9d/2f/aa9d2fe7cf90d0b5300262ac938e7b75.jpg")
        embed.set_image(url = "https://blog.mozilla.org/wp-content/blogs.dir/278/files/2021/08/moz_explains_blue_links_blog_header-1080x720.jpg")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1088445685554225193/1164997266529075251/20231021_003941.jpg?ex=65453f40&is=6532ca40&hm=94a1245721b6846765f18b391fddc1244eb682cf2832d05d06d53949424efd76&")
        
        await iter.response.send_message(embed=embed)

        
def setup(client) -> None:
    client.add_cog(SlashCommands(client))