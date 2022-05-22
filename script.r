library(stats4)

lzipf <- function(s,N) -s*log(1:N)-log(sum(1/(1:N)^s))
fr <- scan("out.txt", what = list(int()))
p <- fr/sum(fr)

ll <- function(s) sum(fr*(s*log(1:2006)+log(sum(1/(1:2006)^s))))

fit <- mle(ll,start=list(s=1))
summary(fit)
s.ll <- coef(fit)

plot(1:2006,p,log="xy", main = "Relative frequency vs Rank (Tweets)", xlab = "
Rank", ylab = "Relative frequency")
lines(1:2006,exp(lzipf(0.671068282103543,2006)),col=2)
lines(1:2006,exp(lzipf(s.ll,2006)),col=3)
rsq <- function(x, y) summary(lm(y~x))$r.squared
rsq(p, exp(lzipf(s.ll,2006)))