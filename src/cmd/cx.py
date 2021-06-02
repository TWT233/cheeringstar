from discord.ext import commands

from client import get_c


@commands.command(name='cx', aliases=['查詢', 'CX'])
async def action(ctx: commands.Context, uid: int):
    print(f'[cmd] cx {ctx.author.id} {uid}')

    try:
        req_result = await get_c(1).call.profile().get_profile(int(uid)).exec()

        u = req_result['user_info']

        ret = (f'''
UID：{u['viewer_id']}，昵稱：{u['user_name']} 
JJC場次：{u['arena_group']}，JJC排名：{u['arena_rank']}
PJJC場次：{u['grand_arena_group']}，PJJC排名：{u['grand_arena_rank']}''')

    except:
        ret = '查询出错，请检查UID是否正确（目前只支持一区）'

    await ctx.send(ctx.author.mention + ret)
    return


@action.error
async def err_uid(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(ctx.author.mention + '''UID错误，请输入九位数字UID，UID不需要每三位分隔。
例如：!cx 123456789''')