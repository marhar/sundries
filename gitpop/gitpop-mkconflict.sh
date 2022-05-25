mkdir x1
git init x1

cd x1
for i in a b; do
  echo first >$i
  git add $i
  git commit -m add-first $i
done

cd ..
git clone x1 x2

cd x1
for i in a b; do
  echo second >$i
  git add $i
  git commit -m add-first $i
done

cd ../x2
for i in a b; do
  echo third >$i
  git add $i
  git commit -m add-first $i
done


