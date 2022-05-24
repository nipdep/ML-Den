from h2o_wave import main, app, Q, ui, data


@app('/demo')
async def serve(q: Q):
    if not q.client.initialized:

        if q.user.logo is None:
            q.user.logo, = await q.site.upload(['h2o_logo.png'])
            q.user.logo_height = '50'

            q.user.sam, = await q.site.upload(['sam.png'])
            q.user.sara, = await q.site.upload(['sara.png'])
            q.user.steve, = await q.site.upload(['steve.png'])
            q.user.cb_cc, = await q.site.upload(['cashback_cc.png'])
            q.user.gold_cc, = await q.site.upload(['gold_cc.png'])
            q.user.reward_cc, = await q.site.upload(['reward_cc.png'])

        q.page['meta'] = ui.meta_card(box='',
                                      title='Hyper-Personalization | H2O Wave',
                                      # stylesheet=ui.inline_stylesheet(style),
                                      layouts=[
                                          ui.layout(
                                              breakpoint='l',
                                              width='1600px',
                                              zones=[
                                                  ui.zone(
                                                      name='header', size='75px', direction='row'),
                                                  ui.zone(name='content'),
                                                  ui.zone('footer'),
                                              ])
                                      ])

        q.page['content-header'] = ui.header_card(
            box='header',
            title='Hyper-Personalize UX',  # TODO : to be updated
            subtitle='User Experience Hype-personalization demo',  # TODO : to be updated
            icon='TFVCLogo',
            icon_color='#222',
            items=[
                ui.text(
                    """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
                    """
                ),
                ui.text("<img src='"+q.user.logo+"' width='" + \
                        str(q.user.logo_height)+"px'>"),
            ],
        )

    if q.args.is_better:
        q.user.sara_resp = """Dear <span class="generic" style="display: none; font-weight: bold; text-decoration: underline;">Customer</span><span class="specific" style="display: inline; font-weight: bold; text-decoration: underline;">Sara</span>, Presenting <span class="specific" style="display: inline; font-weight: bold; text-decoration: underline;">Reward Credit Card</span><span class="generic" style="display: none; font-weight: bold; text-decoration: underline;">Cashback Credit Card</span> with exclusive benefits. Apply Now and Get benefits worth $499+ in first year"""
        q.user.sam_resp = """Dear <span class="generic" style="display: none; font-weight: bold; text-decoration: underline;">Customer</span><span class="specific" style="display: inline; font-weight: bold; text-decoration: underline;">Sam</span>, Get 400$ + benefits on the first year with your <span class="specific" style="display: inline; font-weight: bold; text-decoration: underline;">Cashback Credit Card</span><span class="generic" style="display: none; font-weight: bold; text-decoration: underline;">Gold Credit Card</span>. Apply now to get an additional cashback of 100$"""
        q.user.steve_resp = """Dear <span class="generic" style="display: none; font-weight: bold; text-decoration: underline;">Customer</span><span class="specific" style="display: inline; font-weight: bold; text-decoration: underline;">Steve</span>, Earn 10x Bonus Points when you dine or shop with your <span class="specific" style="display: inline; font-weight: bold; text-decoration: underline;">Gold Credit Card</span><span class="generic" style="display: none; font-weight: bold; text-decoration: underline;">Reward Credit Card</span>. Apply now and get a gift voucher of worth 100$"""
    else:
        q.user.sara_resp = "Dear Customer, Presenting Cashback Credit Card with exclusive benefits. Apply Now and Get benefits worth $499+ in first year"
        q.user.sam_resp = "Dear Customer, Get 400$ + benefits on the first year with your Gold Credit Card. Apply now to get an additional cashback of 100$"
        q.user.steve_resp = "Dear Customer, Earn 10x Bonus Points when you dine or shop with your Reward Credit Card. Apply now and get a gift voucher of worth 100$"

    q.page['content'] = ui.form_card(
        box='content',
        items=[
            ui.text("""
<div align="center">
<p style="font-size:40px;"> Experience Hyper-Personalization </p>
</div>
            """),
            ui.inline([ui.toggle(name='is_better', label='', trigger=True,
                      value=q.args.is_better if q.args.is_better else False)], justify='center'),
            ui.text(content=get_table_content(q))
        ]
    )

    await q.page.save()


def get_table_content(q):
    tabel_html = """
<div align="center">
    <table style="width: 70%; height: 600px">
        <colgroup>
            <col style="width: 30%;">
            <col style="width: 50%;">
            <col style="width: 20%;">
        </colgroup>
        <thead>
            <tr class="table-record">
                <th style="font-size:20px;font-family:sans-serif" class="text-center">Users</th>
                <th style="font-size:20px;font-family:sans-serif" class="text-center">Product Visited</th>
                <th style="font-size:20px;font-family:sans-serif" class="text-center">Message Received</th> 
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    <div align="center">
                        <img class="green-border" src="{sara}">
                        <p class="text-center">Sara</p>
                    </div>
                </td>
                <td>
                    <div class="app">
                        <div class="card-set">
                            <div class="card-item">
                                <div class="image-wrapper image-cover">
                                    <img src={cb_cc} alt=""> </img>
                                </div>
                                <p>
                                    <strong> Reward Credit Card </strong>
                                </p>
                            </div>
                            <div class="card-item">
                                <div class="image-wrapper">
                                    <img src={cb_cc} alt=""> </img>
                                </div>
                                <p>
                                    Cashback Credit Card
                                </p>
                            </div>
                            <div class="card-item">
                                <div class="image-wrapper">
                                    <img src={gold_cc} alt=""> </img>
                                </div>
                                <p>
                                    Reward Credit Card
                                </p>
                            </div>
                        </div>
                    </div>
                </td>
                <td>
                    <div class="resp-box" style="display: block;align:center">
                        <p class="">
                            {sara_resp}
                        </p>
                    </div>
                </td>
            </tr>
            <tr>
                <td>
                    <div align="center">
                            <img class="green-border" src="{sam}">
                        <p class="text-center">Sara</p>
                    </div>
                </td>
                <td
                    <div class="app">
                        <div class="card-set">
                            <div class="card-item">
                                <div class="image-wrapper">
                                    <img src={cb_cc} alt=""> </img>
                                </div>
                                <p>
                                    <strong> Reward Credit Card </strong>
                                </p>
                            </div>
                            <div class="card-item">
                                <div class="image-wrapper image-cover">
                                    <img src={cb_cc} alt=""> </img>
                                </div>
                                <p>
                                    Cashback Credit Card
                                </p>
                            </div>
                            <div class="card-item">
                                <div class="image-wrapper">
                                    <img src={gold_cc} alt=""> </img>
                                </div>
                                <p>
                                    Reward Credit Card
                                </p>
                            </div>
                        </div>
                    </div>
                </td>
                <td>
                    <div class="resp-box" style="display: block;">
                        <p class="">
                            {sam_resp}
                        </p>
                    </div>
                </td>
            </tr>
            <tr>
                <td>
                    <div align="center">
                        <img class="green-border" src="{steve}">
                        <p class="text-center">Sara</p>
                    </div>
                </td>
                <td>
                    <div class="app">
                        <div class="card-set">
                            <div class="card-item">
                                <div class="image-wrapper">
                                    <img src={cb_cc} alt=""> </img>
                                </div>
                                <p>
                                    <strong> Reward Credit Card </strong>
                                </p>
                            </div>
                            <div class="card-item">
                                <div class="image-wrapper">
                                    <img src={cb_cc} alt=""> </img>
                                </div>
                                <p>
                                    Cashback Credit Card
                                </p>
                            </div>
                            <div class="card-item">
                                <div class="image-wrapper image-cover">
                                    <img src={gold_cc} alt=""> </img>
                                </div>
                                <p>
                                    Reward Credit Card
                                </p>
                            </div>
                        </div>
                    </div>
                </td>
                <td>
                    <div class="resp-box" style="display: block;">
                        <p class="">
                            {steve_resp}
                        </p>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
<div>
""".format(sara=q.user.sara, sam=q.user.sam, steve=q.user.steve, reward_cc=q.user.reward_cc, gold_cc=q.user.gold_cc, cb_cc=q.user.cb_cc, sara_resp=q.user.sara_resp, sam_resp=q.user.sam_resp, steve_resp=q.user.steve_resp)
    if q.args.is_better:
        tabel_html += """
<style>
    .green-border {
    border: 3px solid #6bb270;
    border-radius: 50%;
    }
    .image-cover {
    border-radius: 50%;
    background: #FFFFFF;
    color : white;
    padding : 10px 15px;   
    }

    .f1xygs3x tr{
        border-bottom: 0px solid;
    }

    .app {
    display: grid;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 20vh;
    }
    .card-set {
    display: flex;
    background-color: #59c372;
    border-radius: 10px;
    width: 350px;
    height: 150px;
    padding: 20px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    }

    .card-item {
    padding: 10px;
    }

    .image-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;

    width: 72px;
    height: 72px;
    border-radius: 50%;

    cursor: pointer;
    }

    .image-wrapper-white {
    background-color: white;
    }

    .card-item img {
    width: 50px;
    }

    .card-item p {
    text-align: center;
    font-size: 14px;
    font-weight: 600;
    color: white;
    font-family:sans-serif;
    }

    .bold-text {
    font-weight: bolder !important;
    }

    .resp-box{
        font-size:16px;
        align-items: center;
        justify-content: center;
        background:#389C92;
        display: flex;
        border-radius: 10px;
        width: 320px;
        height: 150px;
        color:#FFFFFF;
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 10px;
    }

</style>
    """
    else:
        tabel_html += """
<style>.bg-custom{background:#E64215;color:#000}.card-header{background-color:#fdc726}.fs-24{font-size:24px}
    .green-border {
    border: 3px solid #EA5321;
    border-radius: 50%;
    }
    .image-cover {
    border-radius: 50%;
    background: #FFFFFF;
    color : white;
    }

    
    .f1xygs3x tr{
        border-bottom: 0px solid;
    }

    .card-list {
        display: flex;
    }

    .card-list-item {
        width: 100px;
    }

    .app {
    display: grid;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 20vh;
    }
    .card-set {
    display: flex;
    background-color:#E64215;
    border-radius: 10px;
    width: 350px;
    height: 150px;

    padding: 20px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    }

    .card-item {
    padding: 10px;
    }

    .image-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;

    width: 72px;
    height: 72px;

    }

    .image-wrapper-white {
    background-color: white;
    }

    .card-item img {
    width: 50px;
    }

    .card-item p {
    text-align: center;
    font-size: 14px;
    font-weight: 600;
    color: white;
    font-family:sans-serif;
    }

    .bold-text {
    font-weight: bolder !important;
    }

    .resp-box{
        font-size:16px;
        align-items: center;
        justify-content: center;
        display: flex;
        border-radius: 10px;
        width: 320px;
        height: 150px;
        background:#ED6647;
        color:#FFFFFF;
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 10px;
    }

</style>
    """
    return tabel_html
