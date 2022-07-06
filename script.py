import asyncio

console.log('Running')
async def foo():
    output = 1
    while True:
        await asyncio.sleep(1)
        Element("output").write(output)
        output = output + 1
# close the global PyScript pyscript_loader
pyscript_loader.close()
pyscript.run_until_complete(foo())

# f = open(r"C:\Users\Alejandro\Desktop\test_run.txt", "a")
# f.write("Now the file has more content!")
# f.close()
