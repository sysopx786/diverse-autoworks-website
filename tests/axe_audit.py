import asyncio, json, glob, os
from playwright.async_api import async_playwright
AX=open('node_modules/axe-core/axe.min.js').read()
root='/root/diverse-autoworks/docs'
paths=sorted(set('/'+os.path.relpath(os.path.dirname(f),root).replace('.','') .strip('/')+'/' if os.path.dirname(f)!=root else '/' for f in glob.glob(root+'/**/index.html',recursive=True)))
paths=[p.replace('//','/') for p in paths]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); tot={}
        for name,vp in (("desktop",{"width":1440,"height":900}),("mobile",{"width":390,"height":844})):
            pg=await b.new_page(viewport=vp)
            for u in paths:
                await pg.goto("http://localhost:8123"+u); await pg.wait_for_timeout(1800)
                await pg.evaluate(AX)
                r=await pg.evaluate("axe.run({runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','best-practice']}})")
                for v in r['violations']:
                    k=(v['id'],v['impact']); tot.setdefault(k,[]).append((name,u,len(v['nodes']),v['nodes'][0]['html'][:110]))
        print("pages:",len(paths))
        for k,v in tot.items(): print(k,len(v),v[0])
        if not tot: print("axe: no violations")
        await b.close()
asyncio.run(main())
